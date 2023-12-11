from microbit import *
from random import randint as rand
import audio

def roll_display(number):
   if number == 1:
            display.show(Image(
            "00000:"
            "00000:"
            "00900:"
            "00000:"
            "00000"))
   elif number == 2:
            display.show(Image(
            "00000:"
            "00000:"
            "90009:"
            "00000:"
            "00000"))
   elif number == 3:
            display.show(Image(
            "00009:"
            "00000:"
            "00900:"
            "00000:"
            "90000"))
   elif number == 4:
            display.show(Image(
            "90009:"
            "00000:"
            "00000:"
            "00000:"
            "90009"))
   elif number == 5:
            display.show(Image(
            "90009:"
            "00000:"
            "00900:"
            "00000:"
            "90009"))
   elif number == 6:
            display.show(Image(
            "90009:"
            "00000:"
            "90009:"
            "00000:"
            "90009")) 

def roll():
    sleep(5)
    shakepower = int(accelerometer.get_strength() / 30)
    for _ in range(rand(shakepower,shakepower + 12)):
        roll_display(rand(1,6))
        #audio.play(Sound.GIGGLE) doesn't work for V1
        sleep(10)
    roll_display(rand(1,6))
        

while True:
    if accelerometer.was_gesture('shake'):
        roll()