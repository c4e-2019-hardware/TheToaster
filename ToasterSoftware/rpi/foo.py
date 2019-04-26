import RPi.GPIO as GPIO
import time

servoPIN = 36
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
try:
    dlist = [1,2,2.5,5,7.5,10,12.5,13,13.5,13,12.5,10,7.5,5,2.5,2,1]
    for i in dlist:
        p.ChangeDutyCycle(i)
        time.sleep(0.08)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

p.stop()
GPIO.cleanup()