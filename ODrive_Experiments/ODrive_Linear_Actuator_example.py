from ODrive_Linear_Actuator import odrive, start, move_in_procents
from odrive.enums import AxisState

odrives = [odrive.find_any()]

odrv0 = start(odrives[0])

def callback():
    print("callback")
    odrv0.axis0.requested_state = AxisState.IDLE
    print(odrv0.axis0.pos_estimate)

move_in_procents(odrv0, 12.5, 0.01, 0, callback)