from microbit import *
from random import randint as rand
import audio

def roll():

    sleep(5)
    shakepower = int(accelerometer.get_strength() / 30)
    for _ in range(rand(shakepower,shakepower + 12)):
        display.show(rand(1,6))
        #audio.play(Sound.GIGGLE) doesn't work for V1
        sleep(10)
    display.show(rand(1,6))
        

while True:
    if accelerometer.was_gesture('shake'):
        roll()