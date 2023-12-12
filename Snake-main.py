# Imports go at the top
from microbit import *


def search(d:dict, target):
    for name, val in d.items():
        if val == target:
            return name
    

class Snake():

    def __init__(self):
        self.action = "IDLE"
        self.tick_speed = 500
        self.tick_counter = 0
        self.dir = (0,1)
        self.danger = 0

        self.board = {}
        for x in range(1,6):
            for y in range(1,6):
                self.board[(x,y)]=""

        self.board[(3,3)] = "Player"
        
    def move(self):
        x,y = search(self.board,"Player")

        self.board[(x,y)] = ""

        self.board[(x+self.dir[0],y+self.dir[1])] = "Player"

        
    def act(self):
        if self.action == "IDLE":
            pass
        elif self.action == "RIGHT":
            print("right")
            if self.dir == (0,1):
                self.dir = (1,0)
            elif self.dir == (0,-1):
                self.dir = (-1,0)
            elif self.dir == (1,0):
                self.dir = (0,-1)
            elif self.dir == (-1,0):
                self.dir = (0,1)
        elif self.action == "LEFT":
            print("left")
            if self.dir == (0,1):
                self.dir = (-1,0)
            elif self.dir == (0,-1):
                self.dir = (1,0)
            elif self.dir == (1,0):
                self.dir = (0,1)
            elif self.dir == (-1,0):
                self.dir = (0,-1)
        self.move()
        

    def display_board(self):
        rows = {i:"" for i in range(1,6)}
        for i in range(1,6):
            for j in range(1,6):
                current_block = self.board[(i,j)]
                if current_block == "Player":
                    rows[j] += "9"
                else:
                    rows[j] += "0"
                pass
       
        display.show(Image(":".join(rows[i] for i in range(1,6))))     
        

        
        
        
    def main_loop(self):
        if button_a.is_pressed():
            self.action = "LEFT"
        elif button_b.is_pressed():
            self.action = "RIGHT"
        self.tick_counter += 10
        if self.tick_counter >= self.tick_speed:
            self.act()
            self.display_board()
            self.tick_counter = 0
            self.action = "IDLE"
        sleep(10)
# Code in a 'while True:' loop repeats forever

newGame = Snake()

while True:
    newGame.main_loop()
   