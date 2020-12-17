## Use digital inputs and outputs

Now you know the basics, you can learn to control an external LED with the Raspberry Pi Pico, and have it read input from a button.

--- task ---
Use a resistor between about 50 and 330 ohms, an LED and a pair of M-M jumper leads, to connect up your Raspberry Pi Pico board as shown in the image below.

![an LED and resistor connected to the pico](images/single_LED.png)

--- /task ---

The LED is connected to Pin 15, in the example, but if you use a different pin, remember to look up the number in the pinout diagram in [step 2](1.html).

--- task ---

Use the same code as you did to blink the onboard LED, but change the pin number to `15`.

```python
from machine import Pin, Timer
led = Pin(15, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()
	
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
```

--- /task ---

Run your program and your LED should start blinking. If it's not working, then check your wiring, to be sure that the LED is connected.

Next you can try and control the LED using a button.

--- task ---

Add a button to your circuit as shown in the diagram below.

![image of LED and button on a breadboard](images/button_and_LED.png)

--- /task ---

The button is on pin `14`, and is connected to the 3.3V pin on the Raspberry Pi pico. This means when you set up the pin, you need to tell MicroPython that it is an input pin, and needs to be *pulled down*.

--- task ---
Create a new file and add this code.

``` python
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
Run your code and then when you press the button, the LED should toggle on or off. If you hold the button down it will flash.

--- /task ---

--- save ---
