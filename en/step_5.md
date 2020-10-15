## Install Thonny

In this step you will install Thonny or make sure you have the latest version then you will connect to the Raspberry Pi X and run some simple Python code using the Shell. 

--- task ---

Install/update Thonny. 

<mark>Add precise instructions about version etc when we know.</mark> 
![an image](images/example.png)

--- /task ---

--- task ---
Click on `Run` menu and then `Select Interpreter`:

![Run Select Interpreter menu](images/run-select-interpreter.png)

Choose "MicroPython (generic)" from the drop down:

![Choose MicroPython](images/run-select-interpreter.png)

Click 'OK'.

--- /task ---

--- task ---
Click on `Tools` and then `Options`.

![Tools Options menu](images/tools-options.png)

Select your serial port in the drop down. On the Raspberry Pi the serial port will be "Board in FS Mode — Board CDC (/dev/ttyACM0)". 

--- /task ---

--- task ---
Look at the 'Shell' panel at the bottom of the Thonny editor. 

You should see something like this:

![REPL initial connection messages](images/repl-connected.png)

Thonny will now be able to communicate with the Raspberry Pi X using the REPL (read–eval–print loop) which allows you to type in Python code into the Shell and see the output. 


--- collapse ---

---

title: Troubleshooting

---

--- /collapse ---

--- /task ---

--- task ---
Now you can type commands directly into the Shell and they will run on the Raspberry Pi X.

Type the following command:

``` python
print("Hello!")
```
Tap Enter and you will see the output:

![Print Hello output](images/print-hello-output.png)

--- /task ---

--- task ---
MicroPython adds hardware-specific modules such as 'machine' that you can use to program the Raspberry Pi X. 

You're going to create a machine.Pin object corresponding to the onboard LED which can be accessed using GPIO Pin 25. 

Enter the following code, tapping Enter after each line:

``` python
from machine import Pin
led = Pin(25, Pin.OUT)
led.toggle()
```

You should see the onboard LED light up. Type the code to toggle the LED again to turn the LED off. 

``` python
led.toggle()
```

Toggle the LED on and off as many times as you like. 

Tip: You can use the up arrow on the keyboard to quicky re-enter the previous line. 

--- /task ---

If you want to write a longer program then it's best to save it in a file which is what you will do in the next step.


