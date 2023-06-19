import RPi.GPIO as gpio
import time
import sys

#function to pivot the robot left 
def pivot_left(tf):
        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, False)
        gpio.output(15, True)
        time.sleep(tf)
        gpio.cleanup()
