# Imports go at the top
from microbit import *
import radio

radio.on()

# Code in a 'while True:' loop repeats forever
class Controller():
    
    def mainloop():
        if button_a.is_pressed() and button_b.is_pressed():
            radio.send("DriveStart")
            while button_a.is_pressed() and button_b.is_pressed():
                sleep(100)
        
    pass

class Car():

    def mainloop():
        message = radio.receive()
        if not message: return

        if message == "DriveStart":
            display.show(Image.HAPPY)
        elif message == "DriveEnd":
            display.show(Image.SAD)

        sleep(10)
    pass

while True:
    if button_a.was_pressed():
        display.scroll("Control Mode")
        NewControl = Controller()
        while True:
            NewControl.mainloop()
            

    if button_b.was_pressed():
        display.scroll("Drive Mode")
        NewCar = Car()
        while True:
            NewCar.mainloop()

    sleep(10)
            
            