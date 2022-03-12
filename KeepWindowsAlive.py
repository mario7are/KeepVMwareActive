from datetime import datetime, timedelta
from multiprocessing.connection import wait
from pynput.keyboard import Key, Controller
from pynput import mouse
# from pynput import keyboard
import time
import sys
import argparse

class KeepWindowsAlive:

    WAIT_DURATION = 3600 * 8
    POKE_INTERVAL = 10 * 60
    keyboard = Controller()
    start_timestamp = time.time()
    FIXED_DURATION = True

    def __init__(self, fixed_duration, wait_duration, poke_interval):
        self.WAIT_DURATION = int(wait_duration) if wait_duration and int(wait_duration) > 0 else self.WAIT_DURATION
        self.POKE_INTERVAL = int(poke_interval) if poke_interval and int(poke_interval) > 0 else self.POKE_INTERVAL
        self.FIXED_DURATION = bool(fixed_duration) if fixed_duration and not bool(fixed_duration) else self.POKE_INTERVAL
        self.check() 

    
    def check(self):
        keep_going = True
        end_time = self.WAIT_DURATION + self.start_timestamp
        print(" WAIT_DURATION: {} ".format(self.WAIT_DURATION))
        print(" POKE_INTERVAL: {} ".format(self.POKE_INTERVAL))
        print(" FIXED_DURATION: {} ".format(self.FIXED_DURATION))
        print(" end_time: {} ".format(datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')))
        print(" start_timestamp: {} ".format(datetime.utcfromtimestamp(self.start_timestamp).strftime('%Y-%m-%d %H:%M:%S')))
        # print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        while(keep_going):
            time_now = time.time()
            print(" time_now: {} ".format(time_now))
            keep_going = self.POKE_INTERVAL + self.start_timestamp >= time_now
            keep_going = end_time >= time_now
            self.do_something()
            self.sleep()


    def do_something(self):
        # Press and release space
        self.keyboard.press(Key.left)
        self.keyboard.release(Key.right)
        self.keyboard.press(Key.left)
        self.keyboard.release(Key.right)
        self.addMouseListener()

    def on_move(self, x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))
        self.update_start_time()
        return False

    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        self.update_start_time()
        return False

    def on_scroll(self, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))
        self.update_start_time()
        return False

    def addMouseListener(self):
        listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)
        listener.start()

    def sleep(self):
        time.sleep(self.POKE_INTERVAL)

    
    def update_start_time(self):
        """Updates the starttime so that the timer used to stop preventing the screen lock is reset"""
        if not self.FIXED_DURATION:
            self.start_timestamp = time.time()
            print(" start_timestamp: {} ".format(datetime.utcfromtimestamp(self.start_timestamp).strftime('%Y-%m-%d %H:%M:%S')))


print("Argument List: {}".format(sys.argv))
parser = argparse.ArgumentParser(description='Replace config vars in template.')
parser.add_argument("-fixed_duration", help='If set to false the program will restart the end time to according to the last humand interaction')
parser.add_argument("-wait_duration", help='The max seconds the program will be alive (default is 8hrs)')
parser.add_argument("-poke_interval", help='The number of seconds that the program should do something in the machine in order to keep windows alive (default is 10 mins)')
args = parser.parse_args()
KeepWindowsAlive(args.fixed_duration, args.wait_duration, args.poke_interval)
