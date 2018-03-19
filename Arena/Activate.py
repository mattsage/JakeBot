#Activate.py
import time
import os
from gpiozero import LED

led = LED(17)
led2 = LED(18)

os.system("mpg321 ./rw2016_321.mp3")
os.system("mpg321 ./rw2016_activate.mp3")

led.off()
led2.on()

#time.sleep(180)

time.sleep(5)

os.system("mpg321 ./rw2016_cease_opt2.mp3")

led2.off()

os.system("mpg321 ./rw2016_cease_opt2.mp3")


os.system("/home/pi/Pimoroni/speakerphat/test/Stand_by.py")
