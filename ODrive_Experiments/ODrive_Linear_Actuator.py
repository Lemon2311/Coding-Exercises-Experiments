import odrive
from odrive.enums import AxisState, ControlMode
import time

def setup(odrive):
    odrive.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
    return odrive

def setup_velocity_control(odrive):
    odrive.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL
    return odrive

def check_position_delta(odrive, position_delta_margin, delta_time):
    initial_position = odrive.axis0.pos_estimate
    time.sleep(delta_time)
    return abs(odrive.axis0.pos_estimate - initial_position) < position_delta_margin

bounds = {}

def bounds_detection_routine(odrive):
    
    bound_left = None
    bound_right = None

    odrive.axis0.controller.input_vel = 1

    while True:

        print(f"pos:{odrive.axis0.pos_estimate};")

        if(bound_right is None and check_position_delta(odrive, 0.1, 1)):
            odrive.axis0.controller.input_vel = 0
            bound_right = odrive.axis0.pos_estimate
            odrive.axis0.controller.input_vel = -1

        if(bound_right is not None and check_position_delta(odrive, 0.1, 1)):
            odrive.axis0.controller.input_vel = 0
            bound_left = odrive.axis0.pos_estimate
            print(f"bound_left: {bound_left}; bound_right: {bound_right}")
            bounds[odrive.serial_number] = (bound_left, bound_right)
            return odrive

def setup_position_control(odrive):
    odrive.axis0.controller.config.control_mode = ControlMode.POSITION_CONTROL
    return odrive

def sleep_decorator(func):
    def wrapper(*args):
        time.sleep(2)
        return func(*args)
    return wrapper

@sleep_decorator
def move_in_procents(odrive, procent_from_start, position_delta_margin=0.1, sleep_time_before_callback=0, callback=None):
    bound_left, bound_right = bounds[odrive.serial_number]
    commanded_position = bound_left + (bound_right - bound_left) * procent_from_start / 100
    odrive.axis0.controller.input_pos = commanded_position
    
    while True:
        current_position = odrive.axis0.pos_estimate
        if abs(current_position - commanded_position) < position_delta_margin:
            time.sleep(sleep_time_before_callback)
            print(commanded_position)
            if callback is not None:
                callback()
            break

def start(odrive):
    odrive = bounds_detection_routine(
            setup_velocity_control(
                setup(odrive)))
    setup_position_control(odrive)
    return odrive

__all__ = ['odrive', 'start', 'move_in_procents']
