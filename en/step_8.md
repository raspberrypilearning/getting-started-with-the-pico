## Use an analogue input

--- task ---
 
![an image](images/example.png)


--- /task ---

--- task ---

``` python
from machine import ADC
import time

adc = ADC(Pin(26))
while True:
    print(adc.read_u16())
    time.sleep(1)
```

--- /task ---

--- task ---

``` python
from machine import Pin, ADC
adc = ADC(Pin(26))
led2 = Pin(1,Pin.OUT)
while True:
    if adc.read_u16() < 30000: # adjust this value for your lighting conditions
        led2.value(1)
    else:
        led2.value(0)
```

--- /task ---

--- task ---


--- /task ---

--- save ---
