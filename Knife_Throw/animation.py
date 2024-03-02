import bpy
import math

# Parameters for the animation
rotation_speed = -2 * math.pi * 2  # Negative value for the opposite direction
number_of_spins = 2  # Number of complete spins (spin of 180deg)
total_rotation_angle = -2 * math.pi * number_of_spins  # Total rotation angle required

start_frame = 1

# Calculate the end frame based on the number of spins
fps = bpy.context.scene.render.fps  # Frames per second
time_for_spins = total_rotation_angle / rotation_speed
end_frame = int(start_frame + time_for_spins * fps)

# Set the frame range for the animation
bpy.context.scene.frame_start = start_frame
bpy.context.scene.frame_end = end_frame

# Gravity and initial velocity
gravity = 9.81  # Gravitational acceleration (m/s^2)
velocity = -50   # Initial horizontal velocity of the throw (m/s)

# Get the object
cleaver = bpy.data.objects['Cube']  # Replace 'Cube' with your object's name

# Loop through each frame and set the rotation and position
for frame in range(start_frame, end_frame + 1):
    time = (frame - start_frame) / fps

    # Linear rotation (around X-axis, with reversed direction)
    rotation_angle = rotation_speed * time
    cleaver.rotation_euler[0] = rotation_angle  # Rotating on the X-axis

    # Horizontal movement (along Y-axis)
    position_y = velocity * time
    cleaver.location[1] = position_y  # Moving on the Y-axis

    # Vertical movement (along Z-axis) affected by gravity
    position_z = -0.5 * gravity * time**2  # Displacement due to gravity
    cleaver.location[2] = position_z  # Moving on the Z-axis

    # Insert keyframes for rotation and position
    cleaver.keyframe_insert(data_path="rotation_euler", frame=frame)
    cleaver.keyframe_insert(data_path="location", frame=frame)

print("Animation created")
