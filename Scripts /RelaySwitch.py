import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM) # set pin mode
GPIO.setup(2,GPIO.OUT) # use pin 2 for relay and set to output

GPIO.output(2,0)    # turn relay on
sleep(1)            # wait 1 second
GPIO.output(2,1)    # turn relay off

GPIO.cleanup()      # cleanup