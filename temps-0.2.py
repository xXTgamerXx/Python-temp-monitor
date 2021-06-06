import psutil
import time
import sys

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


while True:
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