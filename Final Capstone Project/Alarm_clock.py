# Requirements : pip install pygame
# Save an audio with the name alarm_clock.mp3

from pygame import mixer
import datetime,time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

if __name__ == '__main__':
    t = input("Enter the time in minutes to set Alarm : ")
    secs=int(t)*60
    t = datetime.time(0, int(t))
    init_t = time.time()

    while True:
        if time.time() - init_t > secs:
            print("Enter 'pause' to stop the alarm.")
            musiconloop('alarm_clock.mp3',"pause")
            exit()