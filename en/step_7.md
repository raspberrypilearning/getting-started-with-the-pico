## Use digital inputs and outputs

--- task ---
 
![an image](images/example.png)

--- /task ---

``` python
from machine import Pin, ADC
import time

led = Pin(1, Pin.OUT)
button = Pin(9, Pin.IN, Pin.PULL_UP)

while True:
    if not button.value():
      led.toggle()
      time.sleep(0.5)
```
                                                                             
<mark>Is there a delay() function to use instead of sleep()?</mark>

--- task ---


--- /task ---

--- save ---
