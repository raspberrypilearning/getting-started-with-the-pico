from picozero import LED, Button

led = LED(15)
button = Button(14)

button.when_pressed = led.toggle