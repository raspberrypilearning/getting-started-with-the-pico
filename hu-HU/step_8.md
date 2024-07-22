## A LED fényerejének szabályozása PWM-mel

[**P**ulse **w**idth **m**odulation/impulzus szélesség moduláció](https://en.wikipedia.org/wiki/Pulse-width_modulation), lehetővé teszi, hogy analóg módon viselkedjenek a digitális eszközök, mint pl. a LED-ek. Ez azt jelenti, hogy a LED-et nem csak egyszerűen ki- vagy bekapcsolhatod, hanem a fényerejét is szabályozhatod.

Ehhez használhatod az előző lépésből származó áramkört.

--- task ---

Nyiss egy új fájlt Thonny-ban, és írd be a következő kódot.

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

Mentsd el és futtasd a fájlt. Látnod kell, hogy a LED ciklikusan pulzáló fénnyel világít.

--- /task ---

A **frequency/frekvencia** (`pwm.freq`) jelzi a Raspberry Pi Pico-nak, hogy milyen gyakran kapcsolja be és ki a LED-et.

A "duty cycle/kitöltési tényező" megadja a LED-nek, hogy mennyi ideig kell alkalmanként bekapcsolva lennie. A Raspberry Pi Pico esetében a MicroPythonban ez tartomány `0`-tól `65025`-ig terjedhet. A `65025` az esetek 100%-a lenne, így a LED bekapcsolva maradna. A 32512 körüli érték azt jelzi, hogy csak az idő felében működne.

--- task ---

Játssz a `pwm.freq()` és a `pwm.duty_u16`, valamint a `sleep` paraméterekkel, hogy megértsd, hogyan állíthatod be a LED fényerejét és a pulzálás ütemét.

--- /task ---

--- save ---
