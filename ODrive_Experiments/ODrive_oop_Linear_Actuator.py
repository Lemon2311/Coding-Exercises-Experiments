import odrive
from odrive.enums import AxisState, ControlMode
import time

class Axis:
    def __init__(self, odrv0):
        self.odrv0 = odrv0
        self.bound_left = None
        self.bound_right = None

    def setup(self):
        self.odrv0.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL

    def setup_velocity_control(self):
        self.odrv0.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL

    def check_position_delta(self, position_delta_margin, delta_time):
        initial_position = self.odrv0.axis0.pos_estimate
        time.sleep(delta_time)
        return abs(self.odrv0.axis0.pos_estimate - initial_position) < position_delta_margin

    def bounds_detection_routine(self):
        self.odrv0.axis0.controller.input_vel = 1

        while True:
            print(f"pos:{self.odrv0.axis0.pos_estimate};")

            if (self.bound_right is None and self.check_position_delta(0.1, 1)):
                self.odrv0.axis0.controller.input_vel = 0
                self.bound_right = self.odrv0.axis0.pos_estimate
                self.odrv0.axis0.controller.input_vel = -1

            if (self.bound_right is not None and self.check_position_delta(0.1, 1)):
                self.odrv0.axis0.controller.input_vel = 0
                self.bound_left = self.odrv0.axis0.pos_estimate
                return self.bound_left, self.bound_right

    def setup_position_control(self):
        self.odrv0.axis0.controller.config.control_mode = ControlMode.POSITION_CONTROL

    def move_in_procents(self, procent_from_start):
        self.odrv0.axis0.controller.input_pos = self.bound_left + (self.bound_right - self.bound_left) * procent_from_start / 100


odrives = [odrive.find_any()]

print(odrives)

actuators = [Axis(odrive) for odrive in odrives]

for actuator in actuators:
    actuator.setup()
    actuator.setup_velocity_control()
    print(actuator.bounds_detection_routine())
    actuator.setup_position_control()
    time.sleep(2)
    actuator.move_in_procents(50)