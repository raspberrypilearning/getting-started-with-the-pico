## Add the MicroPython firmware
Next you need to add the latest version of the MicroPython firmware to your Raspberry Pi X. 

--- task ---

Connect a micro USB cable to the Raspberry Pi X, but don't connect the other end to your computer yet. 

![micro USB cable connected](images/micro-usb-cable.png)

Find the BOOTSEL button on your Raspberry Pi X. 

![BOOTSEL Button](images/bootsel-button.png)

Press the BOOTSEL button and hold it while you connect the other end of the micro USB cable to your computer. 

This puts the Raspberry Pi X into USB mass storage device mode. 

--- /task ---

--- task ---
Run or restart Thonny. 

A dialog will pop up to install the latest version of the MicroPython firmware on the Raspberry Pi X. 

Click on the 'Install' button to install the firmware. 

![Firmware close button](images/install-firmware-close.png)

Wait for the installation to complete and click 'Close'.

--- /task ---

You don't need to copy the MicroPython firmware every time you use your Raspberry Pi X. Next time you can just connect the USB cable without pressing the BOOTSEL button. 

<mark>Is this clear? Do we need to mention that you'll need to do it if you program your device using another language and want to switch back to Python? Will Thonny prompt to update when needed?</mark>
