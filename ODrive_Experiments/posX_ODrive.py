import odrive
from odrive.enums import AxisState

def ODrive_Setup():
    global odrv0
    odrv0 = odrive.find_any()
    odrv0.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL

def ODrive_Move_Pos_To_X(X):
    odrv0.axis0.controller.input_pos += X-odrv0.axis0.pos_estimate
    while True:
        print(f"nr:{odrv0.axis0.pos_estimate};")
        if abs(odrv0.axis0.pos_estimate - X) < 0.001:
           print(f"Poz:{odrv0.axis0.pos_estimate}")
           odrv0.axis0.requested_state = AxisState.IDLE
           break

ODrive_Setup()
ODrive_Move_Pos_To_X(21.3)