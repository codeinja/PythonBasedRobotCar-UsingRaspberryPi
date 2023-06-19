import RPi.GPIO as gpio
import time
import sys

#function to move the robot backwards
def reverse(tf):
        gpio.output(7, True)
        gpio.output(11, False)
        gpio.output(13, False)
        gpio.output(15, True)
        time.sleep(tf)
        gpio.cleanup()
