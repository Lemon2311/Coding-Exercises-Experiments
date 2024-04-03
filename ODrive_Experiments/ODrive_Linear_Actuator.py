import odrive
from odrive.enums import AxisState, ControlMode
import keyboard
import time

def setup():
    global odrv0
    odrv0 = odrive.find_any()
    odrv0.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL

def setup_velocity_control():
    odrv0.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL

def check_position_delta(position_delta_margin, delta_time):
    initial_position = odrv0.axis0.pos_estimate
    time.sleep(delta_time)
    return abs(odrv0.axis0.pos_estimate - initial_position) < position_delta_margin

def bounds_detection_routine():

    odrv0.axis0.controller.input_vel = 1

    while True:

        print(f"pos:{odrv0.axis0.pos_estimate};")

        if('bound_right' not in globals() and check_position_delta(0.1, 1)):
            global bound_right
            odrv0.axis0.controller.input_vel = 0
            bound_right = odrv0.axis0.pos_estimate
            odrv0.axis0.controller.input_vel = -1

        if('bound_right' in globals() and check_position_delta(0.1, 1)):
            global bound_left
            odrv0.axis0.controller.input_vel = 0
            bound_left = odrv0.axis0.pos_estimate
            return bound_left, bound_right

setup()
setup_velocity_control()
print(bounds_detection_routine())

def setup_position_control():
    odrv0.axis0.controller.config.control_mode = ControlMode.POSITION_CONTROL

def move_in_procents(procent_from_start):
    odrv0.axis0.controller.input_pos = bound_left + (bound_right - bound_left) * procent_from_start / 100

setup_position_control()
time.sleep(2)
move_in_procents(50)