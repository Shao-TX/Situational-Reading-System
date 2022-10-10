import keyboard
import time

timer = 0
last_timer = 0
freq = 30

counter = 0
while True:
    if keyboard.is_pressed('q'):
        if timer==0:
            print("On!")
        timer = 5 * freq
    
    print(timer)

    if timer>0:
        timer -= 1
        if timer==0:
            print("Off!")

    time.sleep(1/freq)