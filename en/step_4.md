## Add the MicroPython firmware

--- task ---

Find the BOOTSEL button on your Raspberry Pi Pico. 

![BOOTSEL button](images/Pico-bootsel.png)

Press the BOOTSEL button and hold it while you connect the other end of the micro USB cable to your computer. A Raspberry Pi is shown in the image below, but the same applies to any computer.

![USB cable plugged into a Raspberry Pi](images/Pico-Raspberry-Pi-4-Plug.png)

This puts your Raspberry Pi Pico into USB mass storage device mode. 

--- /task ---

--- task ---

Open Thonny. It should look something like this:

![Thonny application](images/thonny-editor.png)

--- /task ---

In the bottom right corner of the Thonny window, you will see the interpreter used to run the code you write in Thonny.

By default, Thonny uses the interpreter on the 'Local' computer (the one running Thonny).

![Status bar showing the current interpreter as 'Local Python 3'](images/thonny-status-bar-interpreter.png)

--- task ---

Click the Python interpreter and select Install MicroPython.

![A menu showing the available interpreters, with MicroPython selected](images/thonny-micropython-pico-menu.png)

--- /task ---

--- task ---

A dialog box will pop up to install the latest version of the MicroPython firmware on your Raspberry Pi Pico. 

Select the variant and the version should be the latest, so leave it set at that.

![Firmware install](images/thonny-install-micropython-pico.png)

Click the **Install** button to copy the firmware to your Raspberry Pi Pico.

Wait for the installation to complete and click **Close**.

--- /task ---

You don't need to update the firmware every time you use your Raspberry Pi Pico. Next time, you can just plug it into your computer without pressing the 'BOOTSEL' button.
