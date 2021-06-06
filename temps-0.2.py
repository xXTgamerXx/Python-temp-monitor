import psutil
import time
import sys
from pynput import keyboard

break_program = False
def on_press(key):
    global break_program
    if key == keyboard.Key.end:
        time.sleep(1)
        print (u"\u001b[0m -----Stopping Program-----")
        print (u"\u001b[31m Highest Temperature:" "°C")
        print(u"\u001b[32m Lowest Temperature:" "°C")
        print(u"\u001b[33m Average Temperature:" "°C")
        print (u"\u001b[0m --------------------------")
        break_program = True
        return False

print(
    "Welcome to CPUtemps!\n"
    "    ###\n"
    "   #####\n"
    "   #####\n"
    "   #####\n"
    "   #####\n"
    "   #####\n"
    "   #####\n"
    u"\u001b[34m""   #####\n"
    u"\u001b[34m""   #####\n"
    u"\u001b[34m""   #####\n"
    u"\u001b[32m""   #####\n"
    u"\u001b[32m""  #######\n"
    u"\u001b[32m"" #########\n"
    u"\u001b[31m"" #########\n"
    u"\u001b[31m""  #######\n"
    u"\u001b[31m""   #####\n"
)
x=float(input(u"\u001b[0m""Time interval in seconds- "))

with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        temps = psutil.sensors_temperatures()
        time.sleep(x)
        for name, entries in temps.items():
            temp=psutil.sensors_temperatures()
            for entry in entries:
                if entry.label == "Tctl":
                    if entry.current > 70:
                        print(u"\u001b[31m", entry.current, "°C   ", end="\r")
                    elif entry.current > 50:
                        print(u"\u001b[33m", entry.current, "°C   ", end="\r")
                    elif entry.current > 30:
                        print(u"\u001b[32m", entry.current, "°C   ", end="\r")
    print()
