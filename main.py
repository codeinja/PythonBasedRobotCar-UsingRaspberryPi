import RPi.GPIO as gpio
import time
import sys
import tkinter as tk
import warnings

from forward import forward
from reverse import reverse
from left import turn_left
from right import turn_right
from pivotr import pivot_right
from pivotl import pivot_left

def show_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Start time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"End time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
        print(f"Uptime: {end_time - start_time} seconds")
        return result
    return wrapper


class initialize:
    #initialize all the gpio pins required to operate the H-Bridge
    def init(self):
        warnings.filterwarnings("ignore",category=RuntimeWarning)
        gpio.setmode(gpio.BOARD)
        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)
        assert gpio.getmode() == gpio.BOARD, "GPIO mode should be BOARD"
        assert gpio.getmode() != gpio.BCM, "GPIO mode should not be BCM"

        assert gpio.gpio_function(11) == gpio.OUT, "GPIO pin 11 should be set to OUT"
        assert gpio.gpio_function(13) == gpio.OUT, "GPIO pin 13 should be set to OUT"
        assert gpio.gpio_function(15) == gpio.OUT, "GPIO pin 15 should be set to OUT"


class robot(initialize):
    def key_input(self,event):

        self.init()
        print('Key:',event.char)
        key_press=event.char
        sleep_time=0.033

        if key_press.lower() == 'w':
            forward(sleep_time)
        elif key_press.lower() == 'a':
            turn_left(sleep_time)
        elif key_press.lower() == 'd':
            turn_right(sleep_time)
        elif key_press.lower() == 's':
            reverse(sleep_time)
        elif key_press.lower() == 'q':
            pivot_left(sleep_time)
        elif key_press.lower() == 'e':
            pivot_right(sleep_time)
        else:
            gpio.cleanup()

    @show_time
    def myrobot(self):
        command=tk.Tk()
        command.bind('<KeyPress>',self.key_input)
        command.mainloop()

try:
    r=robot()
    r.myrobot()

except KeyboardInterrupt:
    print("Quitting...")
    sys.exit()
	
finally:
    warnings.filterwarnings("ignore",category=RuntimeWarning)
    gpio.cleanup()
