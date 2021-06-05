import psutil
import time

while True:
    temps = psutil.sensors_temperatures()
    time.sleep(1)
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
