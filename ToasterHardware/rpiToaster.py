#
#
### This Class MUST be run on the Raspberry Pi platform!
#
class Utilities:
    def __init__(self, left_sensor_pin=17,
                       right_sensor_pin=27,
                       left_survo_pin=22,
                       right_survo_pin=23,
                       left_kill_pin=24,
                       right_kill_pin=25,
                       online_led_pin=12):
        """ Put init stuff here """
        import RPi.GPIO as GPIO
        import time
        self.left_sensor_pin = left_sensor_pin
        self.right_sensor_pin = right_sensor_pin
        self.left_survo_pin = left_survo_pin
        self.right_survo_pin = right_survo_pin
        self.left_kill_pin = left_kill_pin
        self.right_kill_pin = right_kill_pin

    def checkHardware(self):
        return str("I test the hardware")

    def areWeOnline(self):
        """ Are we connected to the internet? """
        from gpiozero import LED
        import socket
        def is_connected(hostname="www.google.com"):
            try:
                host = socket.gethostbyname(hostname)
                s = socket.create_connection((host, 80), 2)
                return True
            except:
                pass
            return False
        red = LED(self.online_led_pin)
        if is_connected():
            red.on()
        else:
            red.off()
        return None

    def triggerPullDown(self, side=None,inDutyCycle=12.5,initValue=2.5):
        """ Stuff goes here to trigger the stop button, which side right? left? who knows """
        try:
            if "left" in side.upper().lower():
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.left_survo_pin, GPIO.OUT)
                p = GPIO.PWM(self.left_survo_pin, 50) # GPIO pin for PWM with 50Hz
            else:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.right_survo_pin, GPIO.OUT)
                p = GPIO.PWM(self.right_survo_pin, 50) # GPIO pin for PWM with 50Hz
            p.start(initValue) # Initialization
            p.ChangeDutyCycle(inDutyCycle)
            p.stop()
            GPIO.cleanup()
            return None
        except Exception as e:
            return str(e.message)

    def triggerStopButton(self, side=None):
        """ Stuff goes here to trigger the pull down servo to pull the toat down, which side right? left? who knows """
        return None

    def isToastDone(self, side=None):
        """ Is the Toast done? and which side? """
        return None