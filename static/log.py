
import RPi.GPIO as GPIO
import time
from datetime import datetime


# Open logfile | write start date & time of the program.
LogFile = open("/home/pi/GarageDeur/Logs/log.txt", "a")
LogFile.write(datetime.now().strftime("--- Program Started -- %d/%m/%Y -- %H:%M ---"))
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


while True:
    time.sleep(1)
    # Garage door open more than 15 minutes, send warning.... || LOOP NEEDS WORK
    if DoorOpenTimer == 1:
        currentTimeDate = datetime.strptime(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        if (currentTimeDate - TimeDoorOpened).seconds > 900 and DoorOpenflag == 0:
            # Work on warning here | Email? | warning is looping, only want it to happen once
            DoorOpenFlag = 1  # work on this too, stop timer?

        # Door status is unknown
    if GPIO.input(SensorTop) == GPIO.LOW and GPIO.input(SensorBottom) == GPIO.LOW:
        logfile = open("/home/pi/GarageDeur/Logs/log.txt", "a")
        logfile.write(datetime.now().strftime("%d/%m/%Y -- %H:%M:%S  -- Door Opening/Closing \n"))
        logfile.close()
        while GPIO.input(SensorTop) == GPIO.HIGH and GPIO.input == GPIO.HIGH:
            time.sleep(0.5)

        # Door is closed
    if GPIO.input(SensorBottom) == GPIO.HIGH:
        logfile = open("/home/pi/GarageDeur/Logs/log.txt", "a")
        logfile.write(datetime.now().strftime("%d/%m/%Y -- %H:%M:%S  -- Door Closed \n"))
        logfile.close()
        DoorOpenTimer = 0

        # Door is Open
    if GPIO.input(SensorTop) == GPIO.HIGH:
        logfile = open("/home/pi/GarageDeur/Logs/log.txt", "a")
        logfile.write(datetime.now().strftime("%d/%m/%Y -- %H:%M:%S  -- Door Open \n"))
        logfile.close()
        DoorOpenTimer = 1
        DoorOpenflag = 0















