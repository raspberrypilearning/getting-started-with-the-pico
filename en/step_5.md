## Install Thonny

In this step you will install Thonny or make sure you have the latest version then you will connect to the Raspberry Pi X and run some simple Python code using the Shell. 

--- task ---

Install/update Thonny. 

<mark>Add precise instructions about version etc when we know.</mark> 
![an image](images/example.png)

--- /task ---

--- task ---
Run Thonny.

--- /task ---

--- task ---

Connect a micro USB cable to the Raspberry Pi X, but don't connect the other end to your computer yet. 

![micro USB cable connected](images/micro-usb-cable.png)

Find the BOOTSEL button on your Raspberry Pi X. 

![BOOTSEL Button](images/bootsel-button.png)

Press the BOOTSEL button and hold it while you connect the other end of the micro USB cable to your computer. 

This puts the Raspberry Pi X into USB mass storage device mode. 

--- /task ---

--- task ---
The status bar at the bottom of Thonny displays the currently selected interpreter such as 'Python 3.9.0', click on it and choose 'MicroPython(Raspberry Pi X)'.  

![Select Interpreter from status bar menu](images/select-interpreter.png)

--- /task ---

--- task ---
A dialog will pop up to install the latest version of the MicroPython firmware on the Raspberry Pi X. 

Click on the 'Install' button to install the firmware. 

![Firmware close button](images/install-firmware-close.png)

Wait for the installation to complete and click 'Close'.

--- /task ---

From now on you can connect the Raspberry Pi X without pressing the BOOTSEL button and select 'MicroPython(Raspberry Pi X)' from the status bar. You will only need to press the BOOTSEL button if you need to update the firmware. 

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

Setting the value of the led to `1` turns it on. 

Enter the following code, tapping Enter after each line:

``` python
from machine import Pin
led = Pin(25, Pin.OUT)
led.value(1)
```

You should see the onboard LED light up. 

Type the code to set the value to 0 to turn the LED off:

``` python
led.value(0)
```

Turn the LED on and off as many times as you like. 

Tip: You can use the up arrow on the keyboard to quickly access previous lines. 

--- /task ---

If you want to write a longer program then it's best to save it in a file which is what you will do in the next step.


