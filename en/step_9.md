## Controlling an LED with an analogue input

The Raspberry Pi Pico has input pins that can received analogue signals. This means that rather than simply the values of `1` and `0` being read (on and off), they can read values in between.

A perfect analogue device to try this with is a portentiometer.

--- task ---
 
Replace the button in your circuit with a potentiometer, and follow the wiring diagram below to connect it to an anlogue pin.

![potentiometer connected with an LED to the pico](images/pot_and_LED.png)

--- /task ---

--- task ---

In a new file in Thonny, you can first read the resistance of the potentiometer.

Add this code to a new file, and then run it.

```python
from machine import ADC, Pin
import time

adc = ADC(Pin(26))

while True:
    print(adc.read_u16())
    time.sleep(1)
```
Turn the potentiometer to see your maximum and minumum values.

They should approximately between `0` and `65025`

--- /task ---

--- task ---

You can now use this value, to control the duty cycle for PWM on the LED.

Change the code to the following, and once you have run it, tune to dial on the potentiometer to control the LED's brightness.

```python
from machine import Pin, PWM, ADC

pwm = PWM(Pin(15))
adc = ADC(Pin(26))

pwm.freq(1000)

while True:
	duty = adc.read_u16()
	pwm.duty_u16(duty)

--- /task ---


--- save ---
