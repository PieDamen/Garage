import os
import RPi.GPIO as GPIO
import time
from datetime import datetime
import sys
import signal

# Open logfile | write start date & time of the program.
LogFile = open("home/pi/GarageDeur/Static/log.txt", "a")
LogFile.write(datetime.now().strftime("--- Program Starting -- %d/%m/%Y -- %H:%M ---"))
LogFile.close()

# Setup GPIO pins and configuration | wait a second after initialization
GPIO.setmode(GPIO.BCM)
SensorBottom = 18
SensorTop = 24
GPIO.setwarnings(False)
GPIO.setup(SensorBottom, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SensorTop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
time.sleep(1)

# Default time
TimeDoorOpened = datetime.strptime(datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S'), '%d-%m-%Y %H:%M:%S')
# Default start status turns timer off
DoorOpenTimer = 0
# Flag door open to start timer when door is open
DoorOpenflag = 1

try:
    while True:
        time.sleep(1)
        # Garage door open more than 15 minutes, send warning....
        if DoorOpenTimer == 1:
            currentTimeDate = datetime.strptime(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
            if (currentTimeDate - TimeDoorOpened).seconds > 900 and DoorOpenflag == 0:
                # Work on warning here | Email?
                DoorOpenFlag = 1 # work on this too, stop timer?

        if GPIO.input(SensorTop) == GPIO.HIGH and GPIO.input == GPIO.HIGH:
            logfile = open("/home/pi/GarageDeur/static/log.txt", "a")
            logfile.write(datetime.now().strftime("%d/%m/%Y -- %H:%M:%S  -- Door Opening/Closing \n"))
            logfile.close()
            while GPIO.input(SensorTop) == GPIO.HIGH and GPIO.input == GPIO.HIGH:
                time.sleep(0.5)
        else:
            # Door is closed
            if GPIO.input(SensorBottom) == GPIO.LOW:
                logfile = open("/home/pi/GarageDeur/static/log.txt", "a")
                logfile.write(datetime.now().strftime("%d/%m/%Y -- %H:%M:%S  -- Door Closed \n"))
                logfile.close()
                DoorOpenTimer = 0

            # Door is Open
            if GPIO.input(SensorTop) == GPIO.LOW:
                logfile = open("/home/pi/GarageDeur/static/log.txt", "a")
                logfile.write(datetime.now().strftime("%d/%m/%Y -- %H:%M:%S  -- Door Open \n"))
                logfile.close()
                DoorOpenTimer = 1
                DoorOpenflag = 0

except KeyboardInterrupt:
    LogFile = open("home/pi/GarageDeur/Static/log.txt", "a")
    LogFile.write(datetime.now().strftime("--- Program Closed -- %d/%m/%Y -- %H:%M ---"))
    LogFile.close()
















