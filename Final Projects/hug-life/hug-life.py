########################
# Name: Mark Apinis
# Date: May 25, 2017
# File: hug-life.py
# Description: A simulation where monsters randomly move around and attack each other
########################

import utils.ui as ui
from random import randrange

# General Constants
NUM_OF_MONSTERS = 2
START_HEALTH = 5
COLOR_DICT = {
    5:"green",
    4:"yellow",
    3:"orange",
    2:"red",
    1:"black"
} # Look at me allowing more than 5 health but only supplying 5 colors! 
  # This won't go wrong sometime later.

# Generation of UI
PROJECT_NAME = "Hug Life"
GRID_SIZE = 5
CANVAS_SIZE = 600

display = ui.SquareField(CANVAS_SIZE, GRID_SIZE, PROJECT_NAME)
win = display.generate()

# Declaration of Space Class
class Space:
    def __init__(self):
        self._color = "white"

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

# Declaration of Monster Class
class Monster(Space):
    def __init__(self):
        self._color = COLOR_DICT[START_HEALTH]
        self._health = START_HEALTH

    def decrHealth(self):
        self._health -= 1
    
    def getHealth(self):
        return self._health

# Creation of blocks list, the array that will hold all the objects until it is placed randomly on the board
blocks = []
for i in range(NUM_OF_MONSTERS):
    blocks.append(Monster())
for i in range(GRID_SIZE ** 2 - NUM_OF_MONSTERS):
    blocks.append(Space())

# Creation of board list
board = []
for i in range(GRID_SIZE):
    temparr = [] # Temporary array for the rows
    for j in range(GRID_SIZE):
        num = randrange(0, len(blocks)) # Randomly selects an object from the blocks list
        temparr.append(blocks[num]) # Adds this object to the row
        blocks.pop(num) # Removes object from blocks list
    board.append(temparr) # Adds row to entire board

display.update(board) # Now that colors are defined, ui can be updated
win.getMouse() # Wait for user input

while(True):
    for i in range(len(board)):
        for j in range(len(board[j])): #Cycles over all spaces
            if(isinstance(board[i][j], Monster)): # If the space is a monster
                deltaI = randrange(-1, 2) # Generates random y movement
                deltaJ = randrange(-1, 2) # Generates random x movement

                if(i + deltaI >= GRID_SIZE or i + deltaI < 0): # Checks if moving that y would put it off board
                    deltaI = 0
                if(j + deltaJ >= GRID_SIZE or j + deltaJ < 0): # Checks if moving that x would put it off board
                    deltaJ = 0

                if(deltaI == 0 and deltaJ == 0):
                    pass # Why do anything if it isn't moving?
                elif(isinstance(board[i + deltaI][j + deltaJ], Monster)): # If what it is moving into is a monster
                    # Attack
                    board[i + deltaI][j + deltaJ].decrHealth() # Decrease health of attacked monster
                    if(board[i + deltaI][j + deltaJ].getHealth() <= 0): # If monster has no health
                        board[i + deltaI][j + deltaJ] = Space() # Replace with Space
                    else:
                        board[i + deltaI][j + deltaJ].setColor(COLOR_DICT[board[i + deltaI][j + deltaJ].getHealth()])
                        # If it still has health, choose health based on health
                else:
                    board[i][j], board[i + deltaI][j + deltaJ] = board[i + deltaI][j + deltaJ], board[i][j]
                    # If it isn't a monster, move to that space by switching places in list
                
                display.update(board) # Now that something has happened, the board needs to be updated

    # Check how many monsters are left
    monsNum = 0 
    for i in range(len(board)):
        for j in range(len(board[j])):
            if(isinstance(board[i][j], Monster)):
                monsNum += 1

    if(monsNum <= 1): # If there is only one monster left,
        break # End game loop

win.getMouse()
win.close()