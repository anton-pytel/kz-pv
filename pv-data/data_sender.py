import shlex
import sys
import json
import time
import paho.mqtt.client as mqtt
import persistqueue
from epevermodbus.driver import EpeverChargeController
from decouple import config

mqtt_host = config("MQTT_HOST", default="sense.camp")
mqtt_port = config("MQTT_PORT", default=8883)
mqtt_token = ""
queue_name = "solar-data-1"
epever_addr = "/dev/ttyACM0"

def init_mqtt() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.", rc)
    def on_log(client, userdata, level, buf):
        print("log: ",buf) 
    mc = mqtt.Client()
    mc.on_connect = on_connect
    mc.on_disconnect = on_disconnect
    mc.on_log =  on_log
    mc.username_pw_set(mqtt_token, None)
    mc.connect_async(mqtt_host, mqtt_port, 60)
    mc.loop_start()
    return mc

def mqtt_publish(mq: mqtt, data: dict) -> None:
    mqi = mq.publish("v1/devices/me/telemetry", json.dumps(data))
    print(mqi.rc, mqi.is_published())
    mqi.wait_for_publish()

def read_solar_data(ecc: EpeverChargeController) -> dict:
    return {
        "load_power": ecc.get_load_power(),
        "batt_soc": ecc.get_battery_state_of_charge(),
        "batt_power": ecc.get_battery_power(),
        "pv_power": ecc.get_solar_power(),
    }

def init_queue() -> persistqueue:
    return  persistqueue.SQLiteQueue(queue_name, auto_commit=True)

def kill_mqtt(mc: mqtt) -> None:
    mc.loop_stop()

def init_epver() -> EpeverChargeController:
   return EpeverChargeController(epever_addr, 1)

def main() -> int:
    try:
        mc = init_mqtt()
        pq = init_queue()
        sc = init_epver()
        #  while True:
        sd = read_solar_data(sc)
        pq.put(sd)
        sd = pq.get()
        print(sd)
        time.sleep(60)
        mqtt_publish(mc, sd)
        kill_mqtt(mc)
        return 0
    except KeyboardInterrupt:
        kill_mqtt(mc)
        return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
