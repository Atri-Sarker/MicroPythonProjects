from microbit import *
from random import randint as rand

tools = []
#Rock
tools.append(Image('00000:'
                   '09990:'
                   '99999:'
                   '99999:'
                   '00000'))
#Paper
tools.append(Image.SQUARE)
#Scissors
tools.append(Image.SCISSORS)

while True:
    if button_a.is_pressed():

        #countdown
        for i in range(3,0,-1):
            display.show(i)
            sleep(700)

        #play
        display.show(tools[rand(0,2)])