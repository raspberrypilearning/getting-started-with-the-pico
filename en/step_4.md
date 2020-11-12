## Add the MicroPython firmware
If you have never used MicroPython on your Pico board you will need to add the Micropython firmware. 

--- task ---

Connect a micro USB cable to the Raspberry Pi Pico, but don't connect the other end to your computer yet. 

![micro USB cable connected](images/micro-usb-cable.png)

Find the BOOTSEL button on your Raspberry Pi Pico. 

![BOOTSEL Button](images/bootsel-button.png)

Press the BOOTSEL button and hold it while you connect the other end of the micro USB cable to your computer. 

This puts the Raspberry Pi Pico into USB mass storage device mode. 

--- /task ---

--- task ---
In the bottom right hand corner of the Thonny window, you will see the version of Python, you are currently using. 

![Status bar version](images/thonny-status-bar-version.png)

Click on the Python version and choose "MicroPython (Raspberry Pi Pico)":

![Choose MicroPython](images/thonny-micropython-pico.png)

If you don't see this option then check that you have plugged in your Raspberry Pi Pico. 

--- /task ---

--- task ---
A dialog will pop up to install the latest version of the MicroPython firmware on the Raspberry Pi Pico. 

Click 'Install' button to copy the firmware to the Raspberry Pi Pico. 

![Firmware install](images/thonny-install-micropython-pico.png)

Wait for the installation to complete and click 'Close'.

--- /task ---


--- collapse ---

--- 

title: Firmware installation menu

---

You can also access the firmware installation menu by clicking on 'MicroPython (Raspberry Pi Pico)' in the status bar and choosing 'Configure interpreter ...'

![Configure interpreter menu](images/thonny-configure-interpreter.png)

The interpreter settings will open:

![Configure interpreter settings](images/thonny-install-micropython-pico.png)

Click on 'Install or update firmware'. 

You will be prompted to plug in the Raspberry Pi Pico while holding the BOOTSEL button: 

![Configure interpreter settings](images/thonny-install-micropython-pico.png)

Then you will be able to choose 'Install'

![Firmware install](images/thonny-install-micropython-pico.png)

Wait for the installation to complete and click 'Close'.

--- /collapse ---

You don't need to update the firmware every time you use your Raspberry Pi Pico. Next time you can just plug it in to your computer without pressing the BOOTSEL button.

<mark>Is this clear? Do we need to mention that you'll need to do it if you program your device using another language and want to switch back to Python? Will Thonny prompt to update when needed?</mark>
