#pip install RPi.GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Buzzer:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(21, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
    def autoriser(self):
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
    def interdire(self):
        GPIO.output(21, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)

buz=Buzzer
buz.__init__(0)
#n=2
#while n!=0:
    #GPIO.add_event_detect(10, GPIO.RISING)
    #GPIO.add_event_detect(11, GPIO.RISING)
    #GPIO.add_event_detect(12, GPIO.RISING)
    #GPIO.add_event_detect(13, GPIO.RISING)
    #while True:
        #if GPIO.event_detected(10):
            #buzzer.interdire()
        #elif GPIO.event_detected(11):
            #buzzer.interdire()
        #elif GPIO.event_detected(12):
            #buzzer.interdire()
        #elif GPIO.event_detected(13):
            #buzzer.interdire()
        #while autorisation==False:
            #buzzer.interdire()
        #buzzer.autoriser()
        #if gagner==True:
            #n=2
buz.autoriser()
buz.interdire()
GPIO.cleanup()