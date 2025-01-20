## Use the Shell

Use the Thonny Shell to run some simple Python code on your Raspberry Pi Pico.

--- task ---

Make sure that your Raspberry Pi Pico is connected to your computer and you have selected the MicroPython (Raspberry Pi Pico) interpreter.

--- /task ---

--- task ---

Look at the Shell panel at the bottom of the Thonny editor. 

You should see something like this:

![REPL initial connection messages](images/repl-connected.png)

Thonny is now able to communicate with your Raspberry Pi Pico using the REPL (read–eval–print loop), which allows you to type Python code into the Shell and see the output. 

--- /task ---

MicroPython adds hardware-specific modules, such as `machine`, that you can use to program your Raspberry Pi Pico. 

--- task ---

Enter the following code in the Shell, making sure you tap Enter after each line.

``` python
from picozero import pico_led

pico_led.on()
```

You should see the onboard LED light up. 

![Onboard LED on](images/Pico-onboard-LED.png)

Type the code to turn the LED off.

``` python
pico_led.off()
```

Turn the LED on and off as many times as you like. 

**Tip:** You can use the up arrow on the keyboard to quickly access previous lines. 

--- /task ---

If you want to write a longer program, then it's best to save it in a file. You'll do this in the next step.
