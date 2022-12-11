import keyboard
import mouse

recording = False

def on_f6():
    recording = not recording

def main():
    while True:
        if (recording):
            keyboard.record()
        if (keyboard.is_pressed('f6')):
            on_f6()

if __name__ == "__main__":
	main()
