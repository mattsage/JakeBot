from gpiozero import Robot
from time import sleep

robot = Robot(left=(4, 14), right=(17, 18))

robot.forward() # full speed forwards
robot.forward(0.5) # half speed forwards

robot.backward() # full speed backwards
robot.backward(0.5) # half speed backwards

robot.stop() # stop the motor

robot.value = 0.5 # half speed forwards
robot.value = -0.5 # half speed backwards
robot.value = 0 # stop

robot.reverse() # reverse direction at same speed, e.g...

robot.forward(0.5) # going forward at half speed
robot.reverse() # now going backwards at half speed 

robot.right()

robot.left()
