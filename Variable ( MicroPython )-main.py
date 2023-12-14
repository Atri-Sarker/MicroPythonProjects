# Imports go at the top
from microbit import *

class VariableProgram:

    def __init__(self):
        self.counter = 0

    def on_button_pressed_a(self):
        self.counter += 1

    def on_button_pressed_b(self):
        self.counter -= 1

    def on_button_pressed_ab(self):
        display.scroll(self.counter)

Main = VariableProgram()
# Code in a 'while True:' loop repeats forever
while True:
    
    if button_a.was_pressed():
        Main.on_button_pressed_a()

    if button_b.was_pressed():
        Main.on_button_pressed_b()

    if button_a.is_pressed() and button_b.is_pressed():
        Main.on_button_pressed_ab()

    sleep(5)

    
