import odrive
from odrive.enums import AxisState
import time

def ODrive_Setup():
    global odrv0
    odrv0 = odrive.find_any()
    odrv0.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
    print(f"nr:{odrv0.serial_number};V:{odrv0.vbus_voltage};Poz:{odrv0.axis0.pos_estimate}")

ODrive_Setup()
odrv0.axis0.controller.input_pos = 205

while True:
    odrv0.axis0.controller.input_pos +=0.05
    time.sleep(1)


#range_lower_baund = 52.45
#range_upper_baund = 156.45

#def move(procent_from_start):
#    odrv0.axis0.controller.input_pos = range_lower_baund + (range_upper_baund - range_lower_baund) * procent_from_start / 100

#move(85)