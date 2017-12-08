#!/usr/bin/python
#based on Matt Hawkins' code http://www.raspberrypi-spy.co.uk/?p=1101
#Re-written by Matthew Sage for Pimoroni Explorer pHat

import cwiid
import time
import explorerhat as eh

button_delay = 0.1

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Try to connect to the Wiimote & quit if not found
try:
  wii=cwiid.Wiimote()
  except RuntimeError:
  print "Can't connect to Wiimote"
  quit()

print 'Wiimote connected'
wii.rpt_mode = cwiid.RPT_BTN
 
while True:
  buttons = wii.state['buttons']
  if (buttons & cwiid.BTN_UP):
    #Forwards
  	time.sleep(button_delay)    
	eh.motor.one.forward(100)
	eh.motor.two.forward(100)
   
  elif (buttons & cwiid.BTN_DOWN):
	time.sleep(button_delay)  
	eh.motor.one.backward(100)
	eh.motor.two.backward(100)
  
  elif (buttons & cwiid.BTN_LEFT):
	time.sleep(button_delay)         
	eh.motor.one.forward(100)
	eh.motor.two.backward(100)
   
  elif(buttons & cwiid.BTN_RIGHT):
	time.sleep(button_delay)          
	eh.motor.one.backward(100)
	eh.motor.two.forward(100)
  
  else:
  eh.motor.one.stop()
  eh.motor.two.stop()
      
#press button A to stop all motors
  if (buttons & cwiid.BTN_A):
    time.sleep(button_delay)          
    eh.motor.one.stop()
    eh.motor.two.stop()
