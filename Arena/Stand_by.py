#Stand_by.py
import time
import os
from gpiozero import LED, Button

led = LED(23)
button = Button(22)

led.on()

button.when_pressed = os.system("/home/pi/Pimoroni/speakerphat/test/Activate.py") #If button pressed shutdown pi

#pause()
