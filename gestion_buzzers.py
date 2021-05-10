#pip install RPi.GPIO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Buzzer:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(10, GPIO.IN)
        GPIO.setup(11, GPIO.IN)
        GPIO.setup(12, GPIO.IN)
        GPIO.setup(13, GPIO.IN)
        GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
    def autoriser(self):
        GPIO.add_event_detect(10, GPIO.RISING)
        GPIO.add_event_detect(11, GPIO.RISING)
        GPIO.add_event_detect(12, GPIO.RISING)
        GPIO.add_event_detect(13, GPIO.RISING)
        if GPIO.event_detected(10):
            Buzzer.repondre(1)
        if GPIO.event_detected(11):
            Buzzer.repondre(2)
        if GPIO.event_detected(12):
            Buzzer.repondre(3)
        if GPIO.event_detected(13):
            Buzzer.repondre(4)
    def interdire(self):
        GPIO.remove_event_detect(10)
        GPIO.remove_event_detect(11)
        GPIO.remove_event_detect(12)
        GPIO.remove_event_detect(13)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
    def repondre(self,j):
        if j==1:
            GPIO.output(21, GPIO.HIGH)
        if j==2:
            GPIO.output(22, GPIO.HIGH)
        if j==3:
            GPIO.output(23, GPIO.HIGH)
        if j==4:
            GPIO.output(24, GPIO.HIGH)
buz=Buzzer
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
