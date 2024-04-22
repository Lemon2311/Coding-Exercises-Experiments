from machine import Pin, Timer

led = Pin("LED", Pin.OUT)

led.toggle()

