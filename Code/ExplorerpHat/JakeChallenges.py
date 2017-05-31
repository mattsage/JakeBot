import explorerhat as eh
from time import sleep

eh.motor.one.forward(100)
eh.motor.two.forward(100)

sleep(2)

eh.motor.one.stop()
eh.motor.two.stop()

#Can your figure out how to make your robot do the following:
# * Move Backward
# * Mover for a longer period of time
# * Move Slower
# * Turn Left and Right
