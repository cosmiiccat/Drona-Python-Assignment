import turtle

from config import (
    drone_speed,
    drone_color,
    drone_shape
)

from config import (
    distance,
    angle
)

def setup():
    drone = turtle.Turtle()
    # Set the shape, color, and speed of the drone
    drone.shape(drone_shape)
    drone.color(drone_color)
    drone.speed(drone_speed)

    return drone


def move_forward(distance, drone):
    # Move the drone forward by the distance
    drone.forward(distance)

def move_backward(distance, drone):
    # Move the drone backward by the distance
    drone.backward(distance)

def move_left(angle, drone):
    # Turn the drone left by the angle
    drone.left(angle)

def move_right(angle, drone):
    # Turn the drone right by the angle
    drone.right(angle)

def update(action, drone):

    if action == "w":
        move_forward(distance=distance, drone=drone)

    elif action == "s":
        move_backward(distance=distance, drone=drone)

    elif action == "d":
        move_right(angle=angle, drone=drone)

    elif action == "a":
        move_left(angle=angle, drone=drone)  

def run():
    drone = setup()
    while True:
        key = input('Action:')
        if key in ["w", "s", "a", "d"]:
            update(key, drone)


if __name__ == "__main__":
    run()

