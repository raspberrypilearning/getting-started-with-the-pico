## 用模拟输入控制 LED

您的 Raspberry Pi Pico 具有可以接收模拟信号的输入引脚。 这意味着它不仅能读取 `1` 和 `0`（开和关）的值，还能读取两者之间的值。 这意味着它不仅能读取 `1` 和 `0 `（开和关）的值，还能读取两者之间的值。

电位器是这项活动的理想模拟设备。

\--- task ---

将电路中的按钮替换为电位器。 按照下面的接线图将其连接到模拟引脚。

![将电位计与 LED 连接到 Pico](images/pot_and_LED.png)

\--- /task ---

\--- task ---

在 Thonny 的新文件中，你可以首先读取电位器的阻值。

将这段代码添加到一个新文件中，然后运行它。

```python
from machine import ADC, Pin
import time

adc = ADC(Pin(26))

while True:
    print(adc.read_u16())
    time.sleep(1)
```

旋转电位器来查看你的最大值和最小值。

它们应该大约在 `0` 和 `65025` 之间。

\--- /task ---

\--- task ---

您现在可以使用这个值来控制 LED 上 PWM 的占空比。

将代码更改为以下内容。 运行后，调节电位器上的旋钮以控制LED的亮度。

```python
from machine import Pin, PWM, ADC

pwm = PWM(Pin(15))
adc = ADC(Pin(26))

pwm.freq(1000)

while True:
	duty = adc.read_u16()
	pwm.duty_u16(duty)
```

\--- /task ---

\--- save ---
