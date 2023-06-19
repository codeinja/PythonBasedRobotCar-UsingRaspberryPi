import RPi.GPIO as gpio
import time
import sys

#function to pivot the robot rightwards,that is,one set of wheels on one side move forwards and the other set on other side move in reverse
def pivot_right(tf):
        gpio.output(7, True)
        gpio.output(11, False)
        gpio.output(13, True)
        gpio.output(15, False)
        time.sleep(tf)
        gpio.cleanup()
