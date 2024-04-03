import odrive
from odrive.enums import AxisState, ControlMode
import time

def setup():
    global odrive
    odrive = odrive.find_any()
    odrive.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
    return odrive

def setup_velocity_control(odrive):
    odrive.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL
    return odrive

def check_position_delta(odrive, position_delta_margin, delta_time):
    initial_position = odrive.axis0.pos_estimate
    time.sleep(delta_time)
    return abs(odrive.axis0.pos_estimate - initial_position) < position_delta_margin

def bounds_detection_routine(odrive):

    odrive.axis0.controller.input_vel = 1

    while True:

        print(f"pos:{odrive.axis0.pos_estimate};")

        if('bound_right' not in globals() and check_position_delta(0.1, 1)):
            global bound_right
            odrive.axis0.controller.input_vel = 0
            bound_right = odrive.axis0.pos_estimate
            odrive.axis0.controller.input_vel = -1

        if('bound_right' in globals() and check_position_delta(0.1, 1)):
            global bound_left
            odrive.axis0.controller.input_vel = 0
            bound_left = odrive.axis0.pos_estimate
            print(f"bound_left: {bound_left}; bound_right: {bound_right}")
            return odrive

def setup_position_control(odrive):
    odrive.axis0.controller.config.control_mode = ControlMode.POSITION_CONTROL
    return odrive

def move_in_procents(odrive, procent_from_start):
    odrive.axis0.controller.input_pos = bound_left + (bound_right - bound_left) * procent_from_start / 100

move_in_procents(setup_position_control(bounds_detection_routine(setup_velocity_control(setup()))), 10)
