#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
p1=GPIO.PWM(22,1000)
p2=GPIO.PWM(19,1000)
//轉速調整
p1.start(25)
p2.start(40)

def forward():
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)
def backward():  
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)
def turn_right():
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)
def turn_left():image.png
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(18,GPIO.LOW)image.png
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)
def stop():  
    GPIO.output(19,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
      
if (sys.argv[1])=="g":
    forward()
    print("forward")
    time.sleep(2)
    turn_left()
    print("reverse")
    time.sleep(3)
    stop()
if (sys.argv[1])=="b":
    forward()
    print("forward")
    time.sleep(2)
    turn_left()
    print("turn left")
    time.sleep(1)
    forward()
    print("forward")
    time.sleep(1)
    stop()
if (sys.argv[1])=="k":
    forward()
    print("forward")
    time.sleep(2)
    turn_right()
    print("turn right")
    time.sleep(1)
    forward()
    print("forward")
    time.sleep(1)
    stop()
if (sys.argv[1])=="r":
    forward()
    print("forward")
    time.sleep(2)
    turn_left()
    print("reverse")
    time.sleep(3)
    stop()
if (sys.argv[1])=="s":
    stop()
    print("stop")

