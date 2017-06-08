#-*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

INTAVAL = 3
SLEEPTIME = 2
SENSOR_PIN = 18

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

st = time.time()-INTAVAL

while True:
    print GPIO.input(SENSOR_PIN)
    if(GPIO.input(SENSOR_PIN) == GPIO.HIGH) and (st + INTAVAL < time.time()):
        st = time.time()
        print("人を感知しました")

    time.sleep(SLEEPTIME)

