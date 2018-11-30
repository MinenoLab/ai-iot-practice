import RPi.GPIO as GPIO
import time

# GPIOピンをピン番号で指定
GPIO.setmode(GPIO.BOARD)
LED = 11

# GPIO出力の設定
GPIO.setup(LED, GPIO.OUT)

for i in range(3):
    #出力
    GPIO.output(LED, GPIO.HIGH)
    #指定した時間だけ待機
    time.sleep(2)

    GPIO.output(LED, GPIO.LOW)
    time.sleep(1)

#終了処理
GPIO.cleanup()
