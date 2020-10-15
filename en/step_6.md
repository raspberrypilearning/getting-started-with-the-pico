## Blink the onboard LED

The Shell is useful for making sure everything is working and trying out quick commands but it's better to put longer programs in a file. 

Thonny can save and run MicroPython programs directly on the Raspberry Pi X.

In this step you will create a MicroPython program to blink the onboard LED on and off in a loop. 

--- task ---
Click in the main editor pane of Thonny. 

Enter to following code to toggle the LED. 

``` python
from machine import Pin
led = Pin(25, Pin.OUT)

led.toggle()
```

--- /task ---

--- task ---
Click the 'Run' button to run your code. 

Thonny will ask whether you want to save the file on 'This Computer' or the 'MicroPython Device'. Choose 'MicroPython Device'.

![an image](images/save-on-device.png)

Enter 'blink.py' as the file name. 

**Tip:** You do need to enter the '.py' file extension so that Thonny recognises the file as a Python file. 

Thonny will save your program to the Raspberry Pi X and run it. 

You should see the onboard led switch between on and off each time you click the 'Run' button.

--- /task ---

--- task ---
You can use the Timer module to set timer that runs a function at regular intervals. 

Update your code so it looks like this:

``` python
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer(7)

def blink(timer):
  global led
  led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
```

The parameter to the Timer constructor is a timer number from 1 to 14. Some timers are used for specific functions but 7 and above can be used. 

<mark>Is this correct for this implementation of Timer? Which timers can be used?</mark>

Click 'Run' and your program will blink the led on and off until you click the Stop button. 

--- /task ---

<mark>Should we mention the Variables panel in this step?</mark>

<mark>Your file is only saved on the device at this point. What is the best workflow to also save a copy on your computer? Just remember to do 'Save as a copy ...' regularly or is there something better?</mark>

<mark>Is there any way to access the Python files via USB Mass storage mode?</mark>

--- save ---
