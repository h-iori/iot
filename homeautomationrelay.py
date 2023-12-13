import RPi.GPIO as GPIO
import time
#gnd-- 6
#vcc-- 1 (3.3v)
#gpio-- 7
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
Relay_PIN= 7
GPIO.setup(Relay_PIN, GPIO.OUT)
while(1):
    print("bulb on")
    GPIO.output(Relay_PIN,GPIO.LOW)
    time.sleep(1)
    print("bulb off")
    GPIO.output(Relay_PIN, GPIO.HIGH)
    time.sleep(1)
GPIO.cleanup()
