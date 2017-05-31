import explorerhat as eh
from time import sleep

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
