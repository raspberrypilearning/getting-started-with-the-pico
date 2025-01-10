## Blink the onboard LED

The Shell is useful to make sure everything is working and try out quick commands. However, it's better to put longer programs in a file. 

Thonny can save and run MicroPython programs directly on your Raspberry Pi Pico.

Create a MicroPython program to blink the onboard LED on and off in a loop. 

--- task ---

Click in the main editor pane of Thonny. 

Enter the following code to toggle the LED. 

``` python
from picozero import pico_led

while True:
    pico_led.blink()
```

--- /task ---

--- task ---

Click **Run** and the LED will blink on and off.

--- /task ---

--- task ---

Click the **Stop** button.  

--- /task ---

### Save your program to your Pico

--- task ---

Make sure you have Stopped the program, then click the 'Save' icon, or choose 'Save' from the 'File' menu.

--- /task ---

Thonny will give you the option to save the file on **This computer**, or the **Raspberry Pi Pico**. 

![Option buttons to save the file on **This computer** or the **Raspberry Pi Pico**](images/save-on-device.png)

--- task ---
Choose **Raspberry Pi Pico**.
--- /task ---

Enter `blink.py` as the file name and Click 'OK'. 

**Tip:** You need to enter the `.py` file extension so that Thonny recognises the file as a Python file. 

--- /task ---

**Debug**: If you get an error saying the device is busy, you need to first 'Stop' 🛑 the program running on the Pico.