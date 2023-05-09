import os

user_in = int(input("""
Enter a value.

1. shut down
2. sleep
"""))

if  user_in == 1:
    os.system("shutdown /s /t 1")
elif user_in == 2:
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

