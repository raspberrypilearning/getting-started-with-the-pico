## Control LED brightness with PWM

[**P**ulse **w**idth **m**odulation](https://en.wikipedia.org/wiki/Pulse-width_modulation), allows you to give analogue behaviours to digital devices, such as LEDs. This means that rather than an LED being simply on or off, you can control its brightness.

For this activity, you can use the circuit from the last step.

--- task ---

Open a new file in Thonny and add the following code.

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

Save and run the file. You should see the LED pulse bright and dim, in a continuous cycle.

--- /task ---

The **frequency** (`pwm.freq`) tells Raspberry Pi Pico how often to switch the power between on and off for the LED.

The duty cycle tells the LED for how long it should be on each time. For Raspberry Pi Pico in MicroPython, this can range from `0` to `65025`. `65025` would be 100% of the time, so the LED would stay bright. A value of around `32512` would indicate that it should be on for half the time.

--- task ---

Have a play with the `pwm.freq()` values and the `pwm.duty_u16` values, as well as the length of time for the `sleep`, to get a feel for how you can adjust the brightness and pace of the pulsing LED.

--- /task ---

--- save ---
