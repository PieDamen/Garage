#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep


def setup():
    GPIO.setmode(GPIO.BCM) # set pin mode
    GPIO.setup(2,GPIO.OUT) # use pin 2 for relay and set to output


def relay():
    GPIO.output(2,0)    # turn relay on
    sleep(1)            # wait 1 second
    GPIO.output(2,1)    # turn relay off

    GPIO.cleanup()      # cleanup


if  __name__ == '__main__':
    setup()
    try:
        relay()
    except KeyboardInterrupt:
        destroy()