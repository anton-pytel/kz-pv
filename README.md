# Fotovoltika na Komunitnej záhrade Dvory 


V rámci aktivít komunitnej záhrady sa nám podarilo namontovať a spojazdniť [ostrovný systém](https://ecoprodukt.sk/p/80126-solarny-ostrovny-system-1-11kwp-24v-s-40a-mppt-200ah-20179) na výrobu elektrickej energie s pomocou Fotovoltických panelov (PV) 
a vyrobenú energiu uchovávať v batériách. Vďaka za to patrí: 
- [Nadačnému fondu Baumit](https://nadacnyfond.baumit.sk/grantovy-program), ktorý poskytol dotáciu.
- Miroslav K., ktorý poskytol praktické skúsenosti a rady s inštaláciou.
- dobrovoľníci z našej záhrady a z firmy [MAKERS](https://www.makers.sk/), ktorí sa podieľali na inštalácii.

## Krátke vysvetlenie súčastí

![image](https://user-images.githubusercontent.com/15068798/197625625-d6f73895-8b6c-4c43-b057-65e52da12395.png)


![image](https://user-images.githubusercontent.com/15068798/197618093-919877a4-43b4-4854-a60f-8d66810d0a7e.png)

Na prvom obrázku sú zobrazené 3 PV panely.

Na druhom obrázku je zobrazený rozvádzač a jeho súčasti:
- PV: privodné káble z fotovoltických panelov (PV od anglického PhotoVoltaics). Výkon [PV](https://ecoprodukt.sk/p/32035) 3x 370Wp = 1,110kWp
- B: privodné káble z batérií. 2x 12V [batérie](https://ecoprodukt.sk/p/85898-bezudrzbova-bateria-green-cell-agm33-12v-200ah-vrla-31286) s kapacitou 200Ah zapojene do série => 24V napájanie.
- DC: napájanie striedača elektrického prúdu DC=>AC (Direct current = jednosmerný prúd => Alternating current = striedavý prúd). Na vstupe 24V na výstupe 200V. Striedač je to čierne zariadenie.
- AC: elektrické zásuvky ako ich poznáme na výstupe zo striedača.
- Zariadenie, do ktorého sa zbiehajú PV, B a DC káble sa nazýva regulátor nabíjania ([nabíjač](https://ecoprodukt.sk/p/18274)). Slúži na optimálny odber výkonu z PV panelov a presunu do batérii a do zariadení pripojených na striedač.  

**POZOR:** Napätie zo striedača na zásuvkách sa pohybuje na úrovni 200V bez záťaže. V bežne dodávanej elektrickej energie je napätie na úrovni 220-240V. Preto používanie zariadení citlivých na úroveň napätia je na vlastné riziko. Za spôsobené škody na zariadeniach nemôžeme brať zodpovednosť. Rovnako výkon, ktorý je možné odoberať je obmedzený na 960W.


## Návod na obsluhu

### Zapnutie

Kľúč od rozvodnej skrine je v plechovej búde na rohu regálu.

![image](https://user-images.githubusercontent.com/15068798/197621239-0cab31c8-1ec0-4aba-b4f5-f8f29037412c.png)

![IMG_20221105_153353](https://user-images.githubusercontent.com/15068798/201234565-4e3eb196-f537-4e06-a7bb-1e5361687cea.jpg)


Na to, aby bolo možné používať zásuvky, ktoré sú vyvedené von z rozvodnej skrine je potrebné:
1. Skontrolovať, či je zapnutý striedač v polohe ON, indikované svietiacou zelenou LED diodou (zelené svetielko)
2. Skontrolovať, či je v polohe hore prúdový chránič.
3. Skontrolovať, či je v polohe hore 6A istič. 

Ak áno, je možné, zásuvky používať. V prípade problému otvorte [stránku na nahlasovanie problémov](https://github.com/anton-pytel/kz-pv/issues) stlačte tlačitko `New Issue`, napíšte detaily problému do pripraveného okna a popis problému uložte.



### Vypnutie
Je potrebné aspoň jeden z komponentov (chránič, istič) v bodoch uvedených vyššie, vypnúť a zatvoriť rozvodnú skriňu.


## Záver
Na  stránke dodavateľa [produktu](https://ecoprodukt.sk/p/80126-solarny-ostrovny-system-1-11kwp-24v-s-40a-mppt-200ah-20179) je uvedená predpokladaná výroba elektrickej energie. Ročná výroba elektrickej energie daného systému pri optimálnych podmienkach by vedela pokryť takmer jeden celý byt. Poďme ju teda spolu pouužívať. 
Na Displeji striedača sa priebežne menia zobrazené hodnoty. Jediná hodnota v percentách (%) je úroveň nabitia batérii. V prípade hodnoty (nabitia) menej ako 10% zásuvky nepoužívať.
Aktuálny **stav nabitia a história merania** je dostupná na nasledujúcom [odkaze](https://sense.camp/dashboard/dab20c20-6146-11ed-968b-252832edc0fa?publicId=a67eb480-6146-11ed-968b-252832edc0fa).



## PS
Najbližšie plány:

- natiahnutie svetla do železnej búdy
- ďalšie rôzne nepomenované nápady... neváhajte zadávať prostredníctvom [rovnakého formuláru](https://github.com/anton-pytel/kz-pv/issues) ako v prípade problému.

