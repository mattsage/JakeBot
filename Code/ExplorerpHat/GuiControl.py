import explorerhat
from time import sleep
from guizero import App, PushButton

def forwards():
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.forward(100)
    sleep(2)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def backwards():
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def right():
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.forward(100)
	sleep(1.12)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def left():
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)
	sleep(1.12)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

app = App("Mio controller")

Goforwards = PushButton(app, forwards, text="Forwards")
reverse = PushButton(app, backwards, text="Reverse")
TurnRight = PushButton(app, right, text="Right")
TurnLeft = PushButton(app, left, text="Left")

app.display()
