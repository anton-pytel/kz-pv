import shlex
import sys
import json
import time
import paho.mqtt.client as mqtt
import persistqueue
from epevermodbus.driver import EpeverChargeController
from decouple import config

MQTT_HOST = config("MQTT_HOST", default="sense.camp")
MQTT_PORT = config("MQTT_PORT", default=8883)
MQTT_TOKEN = config("MQTT_TOKEN", default="")
QUEUE_NAME = "solar-data-1"
EPEVER_ADDR = config("EPEVER_ADDR", default="/dev/ttyACM0")


def init_mqtt() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.", rc)
            print("See codes here https://github.com/eclipse/paho.mqtt.python/blob/master/src/paho/mqtt/client.py#L157")

    def on_log(client, userdata, level, buf):
        print("log: ", buf)

    def on_message(client, userdata, message, tmp=None):
        print(" Received message " + str(message.payload)
              + " on topic '" + message.topic
              + "' with QoS " + str(message.qos))
    mc = mqtt.Client(client_id="kz-client")
    mc.on_connect = on_connect
    mc.on_disconnect = on_disconnect
    mc.on_log = on_log
    mc.on_message = on_message
    mc.username_pw_set(MQTT_TOKEN, None)
    mc.tls_set(ca_certs="/home/pi/kz-pv/pv-data/ca_cert.pem")
    mc.connect_async(MQTT_HOST, MQTT_PORT, 60)
    mc.loop_start()
    return mc


def mqtt_publish(mq: mqtt, pq: persistqueue) -> None:

    mqi = mq.publish("v1/devices/me/telemetry", json.dumps({"keepalive": 1}))
    try:
        mqi.is_published()  # this raises exception if not
        while pq.qsize() > 0:
            data = pq.get()
            mq.publish("v1/devices/me/telemetry", json.dumps(data))
    except Exception as e:
        print(e)


def read_solar_data(ecc: EpeverChargeController) -> dict:
    return {
        "load_power": ecc.get_load_power(),
        "batt_soc": ecc.get_battery_state_of_charge(),
        "batt_power": ecc.get_battery_power(),
        "pv_power": ecc.get_solar_power(),
        "pv_voltage": ecc.get_solar_voltage(),
        "batt_temperature": ecc.get_battery_temperature(),
        "controller_temperature": ecc.get_battery_temperature(),
    }


def init_queue() -> persistqueue:
    return persistqueue.SQLiteQueue(QUEUE_NAME, auto_commit=True)


def kill_mqtt(mc: mqtt) -> None:
    mc.loop_stop()


def init_epver() -> EpeverChargeController:
    return EpeverChargeController(EPEVER_ADDR, 1)


def current_milli_time():
    return round(time.time() * 1000)


def main() -> int:
    mc = None
    try:
        mc = init_mqtt()
        pq = init_queue()
        sc = init_epver()
        while True:
            sd = read_solar_data(sc)
            sd = {
                "ts": current_milli_time(),
                "values": sd
            }
            pq.put(sd)
            print(sd)
            time.sleep(60)
            mqtt_publish(mc, pq)
    except KeyboardInterrupt:
        if mc:
            kill_mqtt(mc)
        return 0


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
