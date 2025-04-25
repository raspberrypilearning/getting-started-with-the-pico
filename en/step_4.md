## Add the MicroPython firmware

--- task ---

Download the correct MicroPython UF2 file for your board:

- [Pico](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2){:target="_blank"}

- [Pico W](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2){:target="_blank"}

- [Pico 2](https://micropython.org/download/RPI_PICO2/RPI_PICO2-latest.uf2){:target="_blank"}

- [Pico 2 W](https://downloads.raspberrypi.com/micropython/mp_firmware_unofficial_latest.uf2){:target="_blank"}

--- /task ---

--- task ---

Find the BOOTSEL button on your Raspberry Pi Pico. 

![BOOTSEL button](images/Pico-bootsel.png)

Press the BOOTSEL button and hold it while you connect the other end of the micro USB cable to your computer. A Raspberry Pi is shown in the image below, but the same applies to any computer.

![USB cable plugged into a Raspberry Pi](images/Pico-Raspberry-Pi-4-Plug.png)

This puts your Raspberry Pi Pico into USB mass storage device mode and the Pico will appear as 'RPI-RP2'.

--- /task ---

--- task ---

Drag and drop the MicroPython UF2 file you downloaded onto the RPI-RP2 volume. 

Your Pico will reboot.

--- /task ---

--- task ---

Open Thonny. It should look something like this:

![Thonny application](images/thonny-editor.png)

--- /task ---

In the bottom right corner of the Thonny window, you will see the interpreter used to run the code you write in Thonny.

By default, Thonny uses the interpreter on the 'Local' computer (the one running Thonny).

![Status bar showing the current interpreter as 'Local Python 3'](images/thonny-status-bar-interpreter.png)

--- task ---

Click the Python interpreter and select MicroPython.

--- /task ---

You don't need to update the firmware every time you use your Raspberry Pi Pico. Next time, you can just plug it into your computer without pressing the 'BOOTSEL' button.
