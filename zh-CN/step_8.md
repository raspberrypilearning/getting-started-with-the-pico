## 使用 PWM 控制 LED 亮度

[脉冲宽度调制（PWM）](https://zh.wikipedia.org/wiki/%E8%84%88%E8%A1%9D%E5%AF%AC%E5%BA%A6%E8%AA%BF%E8%AE%8A)允许你让数字设备，比如 LED 灯，表现出类似模拟的行为。 这意味着你可以控制 LED 灯的亮度，而不仅仅是简单的开或关。

在这个活动中，你可以使用上一步的电路。

\--- task ---

在Thonny中打开一个新文件，并添加以下代码。

```python
from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(15))

pwm.freq(1000)

while True:
    for duty in range(65025):
		pwm.duty_u16(duty)
		sleep(0.0001)
	for duty in range(65025, 0, -1):
		pwm.duty_u16(duty)
		sleep(0.0001)
```

\--- /task ---

\--- task ---

保存并运行文件。 你应该会看到 LED 灯亮起和变暗，持续循环。

\--- /task ---

**频率**（ `pwm.freq` ）告诉 Raspberry Pi Pico 切换 LED 电源开和关的频率。

占空比告诉 LED 每次应该亮多长时间。 对于用 MicroPython 编程的 Raspberry Pi Pico ，这个值可以从 `0` 变化到 `65025` 。 `65025` 意味着100%的时间，因此 LED 将保持明亮。 大约 `32512` 的数值则表示它应当开启一半的时间。

\--- task ---

尝试调整 `pwm.freq()` 的数值和 `pwm.duty_u16` 的数值，以及 `sleep` 持续时间的长度，来体会你如何调节脉冲 LED 的亮度和闪烁速度。

\--- /task ---

\--- save ---
