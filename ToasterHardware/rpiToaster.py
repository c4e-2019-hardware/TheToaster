#
#
#
#
class Utilities:
    def __init__(self):
        """ Put init stuff here """

    def checkHardware(self):
        return str("I test the hardware")

    def areWeOnline(self):
        """ Are we connected to the internet? """
        return None

    def triggerStopButton(self, side=None):
        """ Stuff goes here to trigger the stop button, which side right? left? who knows """
        return None

    def triggerPullDown(self, side=None):
        """ Stuff goes here to trigger the pull down servo to pull the toat down, which side right? left? who knows """
        import RPi.GPIO as GPIO
import time

servoPIN = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
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
        
        return None

    def isToastDone(self, side=None):
        """ Is the Toast done? and which side? """
        return None
