#pip install RPi.GPIO
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
n=2
while n!=0:
    GPIO.add_event_detect(10, GPIO.RISING)
    GPIO.add_event_detect(11, GPIO.RISING)
    GPIO.add_event_detect(12, GPIO.RISING)
    GPIO.add_event_detect(13, GPIO.RISING)
    while True:
        if GPIO.event_detected(10):
            GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
        elif GPIO.event_detected(11):
            GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
        elif GPIO.event_detected(12):
            GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
        elif GPIO.event_detected(13):
            GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

GPIO.cleanup()