#!/usr/bin/python3 --> #!/usr/bin/python

import keyboard
# import mouse

recording = False

def on_f6():
    recording = not recording

while True:
    if (recording):
        keyboard.record()
    if (keyboard.is_pressed('F6')):
        on_f6()
    