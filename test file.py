import winsound
import time as t

fixed_time = 10
duration = fixed_time

while duration > 0:
    if duration == fixed_time: print(f"STARTED timer for {fixed_time} SECONDS")
    if duration == fixed_time/2: print(f"HALFWAY THERE {fixed_time / 2}")
    if duration == 1: print("DONE")  

    t.sleep(1)
    duration -= 1

winsound.MessageBeep()