# Imports go at the top
from microbit import *
from random import randint as rand

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
        self.score = 1

        self.board = {}
        for x in range(1,6):
            for y in range(1,6):
                self.board[(x,y)]="E"

        self.board[(3,3)] = "Player"
        self.spawn_food()

    def emptySquares(self):
        res = []
        for name, val in self.board.items():
            if val == "E":
                res.append(name)
        return res

    def spawn_food(self):
        print(1)
        options = self.emptySquares()
        chosen = options[rand(0, len(options)-1)]
        print(chosen)
        self.board[chosen] = "FOOD"

    def within_borders(self, pos:tuple):
        if pos[0] >= 6 or pos[0] <= 0 :
            return False
        if pos[1] >= 6 or pos[1] <= 0 :
            return False
        else:
            return True

    def clean_up(self):
        for name, val in self.board.items():
            if val[0] == "L":
                lifespan = int(val[1:])
                lifespan -= 1
                if lifespan <= 0:
                    self.board[name] = "E"
                else:
                    self.board[name] = "L" + str(lifespan)
    def move(self):
        x,y = search(self.board,"Player")
        target = ((x+self.dir[0],y+self.dir[1]))
 
        if not self.within_borders(target):
            pass
        elif self.board[target] == "FOOD":
            self.spawn_food()
            self.score += 1
            self.board[(x,y)] = "L"+str(self.score)
            self.board[(x+self.dir[0],y+self.dir[1])] = "Player"
        else:
            self.board[(x,y)] = "L"+str(self.score)
            self.board[(x+self.dir[0],y+self.dir[1])] = "Player"
            self.clean_up()


        
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
                elif current_block == "FOOD":
                    rows[j] += "5"
                elif current_block[0] == "L":
                    rows[j] += "8"
                elif current_block == "E":
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
   