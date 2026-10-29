from gpiozero import LED, Button
from signal import pause

led = LED(4)

switch1 = Button(14)
switch2 = Button(15)

switch1.when_pressed = led.on
switch2.when_pressed = led.off

pause()
