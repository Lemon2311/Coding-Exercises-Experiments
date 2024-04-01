import odrive
from odrive.enums import AxisState

odrv0 = odrive.find_any()

odrv0.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
odrv0.axis0.controller.input_pos = 0#-odrv0.axis0.pos_estimate

#while True:

 #   print(f"pos:{odrv0.axis0.pos_estimate};")

  #  if abs(odrv0.axis0.pos_estimate - 0) < 0.001:
   #     print(f"nr:{odrv0.serial_number};"
    #          f"V:{odrv0.vbus_voltage};"
     #         f"Poz:{odrv0.axis0.pos_estimate}")
      #  odrv0.axis0.requested_state = AxisState.IDLE
       # break