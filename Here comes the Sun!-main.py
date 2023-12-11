from microbit import *

sun1 = Image(
        "50505:"
        "07970:"
        "59995:"
        "07970:"
        "50505")

sun2 = Image(
        "30003:"
        "05750:"
        "37773:"
        "05750:"
        "30303")

suns = [sun1, sun2]

while True:
    display.show(suns[0])
    suns = suns[::-1]
    sleep(200)
