# python Alarm
import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    soundfile= "papaya.mp3"
    is_runing = True

    while is_runing:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        
        if(current_time == alarm_time):
            print("Wake Up! pookie")
            pygame.mixer.init()
            pygame.mixer.music.load(soundfile)
            pygame.mixer.music.play()

            while pygame.mixer_music.get_busy():
                time.sleep(1)

            is_runing = False

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS) : ")
    set_alarm(alarm_time)