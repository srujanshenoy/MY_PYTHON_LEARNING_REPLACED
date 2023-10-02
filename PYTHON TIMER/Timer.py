import winsound
from time import sleep
import tkinter


def timer_input():
    usr_in = 'wrong'

    while True:
        usr_in = input("Time Duration: ")
        duration, mode = usr_in.split(' ', 1)
        try: duration = float(duration)
        except: pass

        if mode in ['m','s', 'h']:
            if mode == 'h':
                return duration * 3600

            if mode == 'm':
                return duration * 60

            if mode == 's':
                return duration


def timer(Duration: float):
    print("**** TIMER STARTED ****")

    sleep(Duration / 2)
    print("1/2 time remaining")
    winsound.PlaySound('Low Remaining Time.wav', winsound.SND_FILENAME)

    if Duration > 3: sleep(Duration / 2 - 3)
    else: pass
    print("3 SECONDS REMAINING")
    winsound.PlaySound('Low Remaining Time.wav', winsound.SND_FILENAME)

    sleep(1)
    print("2 SECONDS REMAINING")
    winsound.PlaySound('Low Remaining Time.wav', winsound.SND_FILENAME)

    sleep(1)
    winsound.PlaySound('Low Remaining Time.wav', winsound.SND_FILENAME)
    print("1 SECOND REMAINING")

    sleep(1)
    print("TIMES UP!")
    winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
    winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
    winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
    winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)


timer(timer_input())