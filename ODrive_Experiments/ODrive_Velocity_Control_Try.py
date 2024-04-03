import odrive
from odrive.enums import AxisState, ControlMode

odrv0 = odrive.find_any()
odrv0.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
odrv0.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL

odrv0.axis0.controller.input_vel = 1

while True:
    print(f"pos:{odrv0.axis0.pos_estimate};")