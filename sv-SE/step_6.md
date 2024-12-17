## Blinka den inbyggda lysdioden

Shell är användbart för att se till att allt fungerar och prova enkla kommandon. Det är dock bättre att lägga längre program i en fil.

Thonny kan spara och köra MicroPython-program direkt på din Raspberry Pi Pico.

I det här steget kommer du att skapa ett MicroPython-program för att få den inbyggda lysdioden att blinka på och av i en loop.

--- task ---

Klicka i huvudredigeringsfönstret i Thonny.

Skriv in följande kod för att växla lysdioden.

```python
from machine import Pin
led = Pin(25, Pin.OUT)

led.toggle()
```

--- /task ---

--- task ---

Klicka på knappen **Run** för att köra din kod.

Thonny kommer att fråga om du vill spara filen på **This Computer** eller **MicroPython device**. Välj **MicroPython device**.

![Möjlighet att spara filen på This Computer eller MicroPython device](images/save-on-device.png)

Skriv "blink.py" som filnamn.

**Tips:** Du måste ange filtillägget `.py` så att Thonny känner igen filen som en Python-fil.

Thonny kan spara ditt program till din Raspberry Pi Pico och köra det.

Du bör se den inbyggda lysdioden växla mellan på och av varje gång du klickar på knappen **Run**.

--- /task ---

--- task ---

Du kan använda "Timer"-modulen för att ställa in en timer som kör en funktion med jämna mellanrum.

Ändra din kod så att den ser ut så här:

```python
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
```

Klicka på **Run** och ditt program blinkar med lysdioden tills du klickar på **Stop**-knappen.

--- /task ---

--- save ---
