## Digitális be- és kimenetek használata

Most hogy már ismered az alapokat, megtanulhatod a külső LED vezérlését a Raspberry Pi Pico segítségével, és meghatározhatod egy, a bemenetre kötött nyomógomb állapotát.

--- task ---

50 és 330 ohm közötti ellenállást, LED-et és egy pár M-M (papa-papa) jumper kábelt használj a Raspberry Pi Pico csatlakoztatásához a lenti képen látható módon.

![LED és ellenállás a Pico-hoz csatlakoztatva](images/single_LED.png)

--- /task ---

Ebben a példában a LED a 15-ös lábhoz csatlakozik. Ha másik lábat használsz, ne felejtsd el megkeresni a számot a [Meet Raspberry Pi Pico szakasz](1.html) lábkiosztás ábráján.

--- task ---

Ugyanazt a kódot használd, mint a panelen lévő LED villogtatásához, de a PIN-számot `15`-re írd át.

```python
from machine import Pin, Timer
led = Pin(15, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()
	
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
```

--- /task ---

Futtasd a programot, a LED-nek villognia kell. Ha nem működik, ellenőrizd a kábelezést, és győződj meg róla, hogy a LED csatlakoztatva van.

Ezután próbáld meg egy gombbal vezérelni a LED-et.

--- task ---

Adj hozzá egy nyomógombot az áramkörödhöz az alábbi ábra szerint.

![LED és gomb a próbapanelen](images/button_and_LED.png)

--- /task ---

A gomb a `14`-es bemenetet, és a Raspberry Pi Pico 3,3 V-os kimenetét köti össze. Ez azt jelenti, hogy amikor beállítod a lábat, meg kell adni a MicroPython-ban, hogy ez egy bemeneti pin, valamint a *pulled down* parancs megadása is szükséges.

--- task ---

Hozz létre egy új fájlt, és add hozzá ezt a kódot.

```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
	    led.toggle()
        time.sleep(0.5)
```

--- /task ---

--- task ---

Futtasd a parancsot, és a gomb megnyomásakor a LED-nek ki- vagy be kell kapcsolnia. Ha lenyomva tartod a gombot, villogni fog.

--- /task ---

--- save ---
