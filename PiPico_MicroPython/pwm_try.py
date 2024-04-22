from machine import Pin, PWM

# Create a PWM object on GPIO 25
pwm = PWM(Pin(18))

# Set the PWM frequency to 5000 Hz
pwm.freq(5000)

# Set the duty cycle to 50%. The value should be in the range 0-65535, so 50% is 32767.
pwm.duty_u16(32767)