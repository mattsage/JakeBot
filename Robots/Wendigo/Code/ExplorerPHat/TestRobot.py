import explorerhat as eh
from time import sleep
from gpiozero import LED
from gpiozero import Servo

#Eyes
led = LED(17) 
led.on()

#Weapons check
axe = Servo(31)
axe.min()
sleep(1)
axe.mid()
sleep(1)
axe.max()
sleep(1)

flipper = Servo(32)
flipper.min()
sleep(1)
flipper.mid()
sleep(1)
flipper.max()
sleep(1)

#Move Forward
eh.motor.one.forward(100)
eh.motor.two.forward(100)

sleep(2)

eh.motor.one.stop()
eh.motor.two.stop()

#Move Backward
eh.motor.one.backward(100)
eh.motor.two.backward(100)

sleep(2)

eh.motor.one.stop()
eh.motor.two.stop()

#Turn Right
eh.motor.one.backward(100)
eh.motor.two.forward(100)

sleep(1.12)

eh.motor.one.stop()
eh.motor.two.stop()

#Turn Left
eh.motor.one.forward(100)
eh.motor.two.backward(100)

sleep(1.12)

eh.motor.one.stop()
eh.motor.two.stop()
