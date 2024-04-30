from machine import Pin, PWM

pwm = PWM(Pin(21))

pwm.freq(50)

pwm.duty_u16(7000)