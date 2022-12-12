#!/usr/bin/python3 --> #!/usr/bin/python

import keyboard
import mouse
import time
import pyautogui

recording = False

def on_f6():
    recording = not recording

def main():
    time.sleep(3)
    # keyboard.press_and_release('TAB')
    while True:
        script()
        time.sleep(20)
            
def script():
    hit_shell()
    move_right(1.2)
    move_forward(0.25)
    hit_shell()
    move_right(1.3)
    move_forward(0.03)
    hit_shell()
    move_left(0.45)
    move_back(1.352)
    hit_shell()
    move_forward(0.21)
    move_left(1.43)
    hit_shell()
    move_left(0.5055)
    move_forward(0.8529)
    # move_to_new_server()

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
    time.sleep(20)
    mouse.release('left')
    keyboard.press_and_release('c')
    
def move_to_new_server():
    keyboard.press_and_release('z')
    mouse.move(290, -200, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.drag(0, 0, 0, 500, absolute=False, duration=0.1)
    time.wait(1)
    mouse.move(200, 84, absolute=False, duration=1)
    mouse.move(20, 0, absolute=False, duration=0.1)
    mouse.move(-40, 0, absolute=False, duration=0.1)
    mouse.move(20, 0, absolute=False, duration=0.1)
    mouse.move(-20, 0, absolute=False, duration=0.1)
    mouse.click('left')
# keyboard.add_hotkey(37, print, args=('left arrow was pressed'))

main()