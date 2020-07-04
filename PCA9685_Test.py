import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
for i in range(180):
    kit.servo[0].angle = i*10
    time.sleep(0.01)

