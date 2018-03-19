#Stand_by.py
import time
import os
from gpiozero import LED, Button

led = LED(17)
button = Button(3)

led.on()

button.when_pressed = os.system("/home/pi/Pimoroni/speakerphat/test/Activate.py") #If button pressed shutdown pi

#pause()
