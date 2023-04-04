# Created by: Cristiano S
# Created in: April 2023
#
# Uses a distance sensor to control when a servo moves

import time
import board
import adafruit_hcsr04
import pwmio
from adafruit_motor import servo

# Create a sonar on pin GP2 for trig and pin GP3 for echo
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP2, echo_pin=board.GP3)

# Create a PWMOut object on Pin GP4
pwm = pwmio.PWMOut(board.GP4, duty_cycle=2 ** 15, frequency=50)

# Create a servo object called my_servo.
my_servo = servo.Servo(pwm)

while True:
    try:
        print(sonar.distance)
        if sonar.distance < 50:
            print("Start servo")
            for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
                my_servo.angle = angle
                time.sleep(0.05)
            for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
                my_servo.angle = angle
                time.sleep(0.05)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)