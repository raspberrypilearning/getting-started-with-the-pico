## Control an LED with an analogue input

Your Raspberry Pi Pico has input pins that can receive analogue signals. This means that instead of only reading the values of `1` and `0` (on and off), it can read values in between.

A potentiometer is the  perfect analogue device for this activity. 

--- task ---
 
Replace the button in your circuit with a potentiometer. Follow the wiring diagram below to connect it to an analogue pin.

![Potentiometer connected with an LED to the Pico](images/pot_and_LED.png)

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

Turn the potentiometer to see your maximum and minimum values.

They should be approximately between `0` and `65025`.

--- /task ---

--- task ---

You can now use this value to control the duty cycle for PWM on the LED.

Change the code to the following. Once you have run it, tune the dial on the potentiometer to control the LED's brightness.

```python
from machine import Pin, PWM, ADC

pwm = PWM(Pin(15))
adc = ADC(Pin(26))

pwm.freq(1000)

while True:
	duty = adc.read_u16()
	pwm.duty_u16(duty)
```

--- /task ---


--- save ---
