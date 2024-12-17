## Styr lysdiodens ljusstyrka med PWM (Pulsvariation)

[**P**ulse **w**idth **m**odulation](https://en.wikipedia.org/wiki/Pulse-width_modulation), låter dig ge analoga beteenden till digitala enheter, som t.ex. lysdioder. Detta innebär att du kan styra ljusstyrkan i stället för att en lysdiod är på eller av.

För denna aktivitet kan du använda kopplingen från förra steget.

--- task ---

Öppna en ny fil i Thonny och lägg till följande kod.

```python
from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(15))

pwm.freq(1000)

while True:
    for duty in range(65025):
		pwm.duty_u16(duty)
		sleep(0.0001)
	for duty in range(65025, 0, -1):
		pwm.duty_u16(duty)
		sleep(0.0001)
```

--- /task ---

--- task ---

Spara och kör filen. Du bör se lysdioden pulsera starkt och svagt, i en kontinuerlig cykel.

--- /task ---

**frequency** (`pwm.freq`) talar om för Raspberry Pi Pico hur ofta strömmen ska slås på och av för lysdioden.

**duty**-loopen talar om för lysdioden hur länge den ska lysa varje gång. För Raspberry Pi Pico i MicroPython kan detta variera från `0` till `65025`. "65025" är 100 % av tiden, så lysdioden lyser kontinuerligt. Ett värde på runt "32512" betyder att den är på halva tiden.

--- task ---

Test med olika `pwm.freq()`-värden och `pwm.duty_u16`-värden, samt längden på tiden för `sleep`, för att få en känsla för hur du kan justera ljusstyrkan och takten för pulserande LED.

--- /task ---

--- save ---
