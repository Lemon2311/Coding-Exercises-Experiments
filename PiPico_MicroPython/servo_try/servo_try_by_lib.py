from machine import Pin
from servo import Servo # using servo library

servo = Servo(Pin(21))

servo.move(180) # move in deg