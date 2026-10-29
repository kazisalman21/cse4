from gpiozero import LED, Button
import time

led = LED(4)
button = Button(14)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()

    time.sleep(0.1)
