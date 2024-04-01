import odrive
from odrive.enums import AxisState

odrv0 = odrive.find_any()

print(f"nr:{odrv0.serial_number};V:{odrv0.vbus_voltage};Poz:{odrv0.axis0.pos_estimate}")

odrv0.axis0.requested_state = AxisState.IDLE
