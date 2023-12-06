from microbit import *

delay_interval = 100
loop_size = 4

while True:
    if button_a.is_pressed():
        for x in range(loop_size):
            display.show(Image.SURPRISED)
            sleep(delay_interval)
            display.clear()
            sleep(delay_interval)
    if button_b.is_pressed():
        for x in range(loop_size):
            display.show(Image.ASLEEP)
            sleep(delay_interval)
            display.clear()
            sleep(delay_interval)