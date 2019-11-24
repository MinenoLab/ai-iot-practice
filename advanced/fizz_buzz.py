#coding:utf-8 
import RPi.GPIO as GPIO 
import time 
# GPIOピンをピン番号で指定 
GPIO.setmode(GPIO.BOARD) 

fizz_led = 11 
buzz_led = 12 

# GPIO出力の設定 
GPIO.setup(buzz_led, GPIO.OUT) 

for count in range(1, 30): 
    if count % 15 == 0: 
        print("FizzBuzz") 
        GPIO.output(fizz_led, GPIO.HIGH) 
        GPIO.output(buzz_led, GPIO.HIGH) 
        time.sleep(1) 
    elif count % 3 == 0: 
        print("Fizz") 
        GPIO.output(fizz_led, GPIO.HIGH) 
        time.sleep(1) 
    elif count % 5 == 0: 
        print("Buzz") 
        GPIO.output(buzz_led, GPIO.HIGH) 
        time.sleep(1) 
    else: 
        print(count) 
        time.sleep(1) 
    GPIO.output(buzz_led, GPIO.LOW) 
    GPIO.output(fizz_led, GPIO.LOW) 

GPIO.cleanup() # GPIOを解放 
