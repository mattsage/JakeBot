from gpiozero import Motor, OutputDevice
from time import sleep

#Motor Setup
motor1 = Motor(24, 27)
motor1_enable = OutputDevice(5, initial_value=1)
motor2 = Motor(6, 22)
motor2_enable = OutputDevice(17, initial_value=1)
motor3 = Motor(23, 16)
motor3_enable = OutputDevice(12, initial_value=1)
motor4 = Motor(13, 18)
motor4_enable = OutputDevice(25, initial_value=1) 


motor.forward() # full speed forwards
motor.forward(0.5) # half speed forwards

motor.backward() # full speed backwards
motor.backward(0.5) # half speed backwards

motor.stop() # stop the motor

motor.value = 0.5 # half speed forwards
motor.value = -0.5 # half speed backwards
motor.value = 0 # stop

motor.reverse() # reverse direction at same speed, e.g...

motor.forward(0.5) # going forward at half speed
motor.reverse() # now going backwards at half speed 
