# Imports go at the top
from microbit import *

class VariableProgram:

    def __init__(self):
        self.hunger = 0

    def on_button_pressed_a(self):
        self.hunger += 1
        display.scroll(self.hunger)

    def on_button_pressed_b(self):
        self.hunger = 0
        display.scroll(self.hunger)

Main = VariableProgram()
# Code in a 'while True:' loop repeats forever
while True:
    
    if button_a.was_pressed():
        Main.on_button_pressed_a()

    if button_b.was_pressed():
        Main.on_button_pressed_b()

    sleep(5)
