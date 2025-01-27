## Use digital inputs and outputs

Now you know the basics, you can control an external LED with your Raspberry Pi Pico, and get it to read input from a button.

--- task ---

If you have a breadboard, put your Raspberry Pi Pico on the board.

Place it so that the two headers are separated by the ravine in the middle.

--- /task ---

Connect the LED to pin 15.

--- task ---

Use a resistor between about 50 and 330 ohms, an LED, and a pair of pin-to-pin jumper leads to connect up your Raspberry Pi Pico on a breadboard, as shown in this image.

The LED's long leg is at the bottom.

![LED and resistor connected to the Pico](images/single_LED.png)

--- /task ---

--- task ---

Create a new file and add this code.

```python
from picozero import LED

led = LED(15)

while True:
    led.blink()
```

**Notice** you now `import LED` rather than `import pico_led`, as you want to control an LED connected to a GPIO pin.

--- /task ---

--- task ---

Run your program and your LED should start to blink. If it's not working, check your wiring to be sure that the LED is connected.

--- /task ---

--- task ---

Stop your program.

--- /task ---

### Control the LED with a button

--- task ---

Add a button to your circuit as shown in this diagram.

![LED and button on a breadboard](images/button_and_LED.png)

--- /task ---

The button is connected to GPIO pin `14`.

--- task ---

Create a new file and add this code.

```python
from picozero import LED, Button

led = LED(15)
button = Button(14)

button.when_pressed = led.toggle
```

--- /task ---

--- task ---

**Run** your code. 

When you press the button, the LED should switch from on to off (or from off to on).

--- /task ---

--- task ---

Stop your program.

--- /task ---

--- save ---
