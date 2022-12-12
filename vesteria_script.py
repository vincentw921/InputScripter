#!/usr/bin/python3 --> #!/usr/bin/python

import keyboard
import mouse
import time
import sys

recording = False

def on_f6():
    recording = not recording

def main():
    time.sleep(3)
    # keyboard.press_and_release('TAB')
    while True:
        script()
            
def script():
    hit_shell()
    move_right(1.2)
    move_forward(0.25)
    hit_shell()
    move_right(1.33)
    move_forward(0.3)
    hit_shell()
    move_left(0.5)
    move_back(1.4)
    hit_shell()
    move_forward(0.2)
    move_left(1.45)
    hit_shell()
    move_left(0.53)
    move_forward(0.85)
    # keyboard.press_and_release('caz')
    # mouse.move(100, 100, absolute=False, duration=0.2)
    # mouse.move(-100, -100, absolute=False, duration=0.2)
    # mouse.click('left')
    # mouse.move(200, 100, absolute=False, duration=0.2)
    # mouse.click('left')

def turn_90_left():
    keyboard.press('left arrow')
    time.sleep(2)
    keyboard.release('left arrow')
    
def turn_90_right():
    keyboard.press('right')
    time.sleep(2)
    keyboard.release('right')

def move_forward(move_time):
    keyboard.press('w')
    time.sleep(move_time)
    keyboard.release('w')

def move_back(move_time):
    keyboard.press('s')
    time.sleep(move_time)
    keyboard.release('s')

def move_left(move_time):
    keyboard.press('a')
    time.sleep(move_time)
    keyboard.release('a')

def move_right(move_time):
    keyboard.press('d')
    time.sleep(move_time)
    keyboard.release('d')
    
def hit_shell():
    mouse.press('left')
    time.sleep(1)
    mouse.release('left')
    keyboard.press_and_release('c')

# keyboard.add_hotkey(37, print, args=('left arrow was pressed'))

main()
# time.sleep(3)
# turn_90_left()