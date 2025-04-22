## Control an LED with an analogue input

Your Raspberry Pi Pico has input pins that can receive analogue signals. This means that instead of only reading the values of `1` and `0` (on and off), it can read values in between.

A potentiometer is the perfect analogue device for this activity. 

--- task ---
 
Replace the button in your circuit with a potentiometer. Follow the wiring diagram below to connect it to GPIO pin 26.

![Potentiometer connected with an LED to the Pico](images/pot_and_LED.png)

--- /task ---

### Dial up the brightness!

--- task ---

Create a new file and add this code.

```python
from picozero import LED, Pot

led = LED(15)
pot = Pot(26)

while True:
    led.value = pot.value
```

--- /task ---

--- task ---

**Run** your program and dial up your potentiometer to change the LED brightness!

--- /task ---

--- task ---

Stop 🛑 the program.

--- /task ---

--- save ---
