import RPi.GPIO as gpio
import time
import sys

#function to move the robot forward
def forward(tf):
        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, True)
        gpio.output(15, False)
        time.sleep(tf)
        gpio.cleanup()
