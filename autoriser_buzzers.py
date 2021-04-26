# pip install RPi.GPIO
import RPi.GPIO as GPIO


class Buzzer:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(21, GPIO.OUT, GPIO.LOW)
        GPIO.setup(22, GPIO.OUT, GPIO.LOW)
        GPIO.setup(23, GPIO.OUT, GPIO.LOW)
        GPIO.setup(24, GPIO.OUT, GPIO.LOW)

    def autoriser(self):
        GPIO.setup(21, GPIO.OUT, GPIO.HIGH)
        GPIO.setup(22, GPIO.OUT, GPIO.HIGH)
        GPIO.setup(23, GPIO.OUT, GPIO.HIGH)
        GPIO.setup(24, GPIO.OUT, GPIO.HIGH)

    def interdire(self):
        GPIO.setup(21, GPIO.OUT, GPIO.LOW)
        GPIO.setup(22, GPIO.OUT, GPIO.LOW)
        GPIO.setup(23, GPIO.OUT, GPIO.LOW)
        GPIO.setup(24, GPIO.OUT, GPIO.LOW)


"""
La fonction interdire sera utilisée lorsqu'on passera à la question suivante
ou lorsqu'un round se terminera ou quand un buzzer sera appuyé.
La fonction autoriser, elle, sera activable via un bouton disponible sur
l'interface animateur.
"""
