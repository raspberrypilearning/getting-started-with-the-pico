## Control LED brightness

For this activity, you can use the circuit from the last step.

### LED fader

--- task ---

Change the last line in your code

```python
from picozero import LED, Button

led = LED(15)
button = Button(14)

button.when_pressed = led.pulse
```

--- /task ---

--- task ---

Run the file. You should see the LED pulse bright and dim, in a continuous cycle.

--- /task ---

--- task ---

Stop your program.

--- /task ---

--- save ---

### Fine brightness control

You can manually set brightness levels.

--- task ---

Create a new file and add this code.

```python
from picozero import LED
from time import sleep

led = LED(15)

while True:
    led.brightness = 0.1  # very dim
    sleep(1)
    led.brightness = 0.5  # half brightness
    sleep(1)
    led.brightness = 1  # full brightness
    sleep(1)
```

--- /task ---

--- task ---

Run the file. You should see the LED brightness change between the three levels set in your code.

--- /task ---

--- task ---

Stop your program.

--- /task ---

--- save ---