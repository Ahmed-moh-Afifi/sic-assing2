import psutil
from time import sleep
from datetime import datetime
from gpiozero import LED

led = {"red": LED(14), "yellow": LED(15), "green": LED(18)}

logFile = open("log.txt", "a")

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=5, percpu=False)
    print(f"CPU usage is: {usage}% {datetime.now()}")
    logFile.write(f"CPU usage is: {usage}% {datetime.now()}\n")

    if usage < 50:
        # green led on
        led["yellow"].off()
        led["red"].off()
        led["green"].on()
        print("Green led on")
    elif usage < 80:
        # yellow led on
        led["green"].off()
        led["red"].off()
        led["yellow"].on()
        print("Yellow led on")
    else:
        # red led on
        led["green"].off()
        led["yellow"].off()
        led["red"].on()
        print("Red led on")

while True:
    check_cpu_usage()
    sleep(5)