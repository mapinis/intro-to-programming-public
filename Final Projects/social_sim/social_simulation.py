########################
# Name: Mark Apinis
# Date: May 25, 2017
# File: social_simulation.py
# Description: A simulation of the Schelling's Model of Segregation 
########################

# Note: A lot in this file is incorrect. I didn't use proper encapsulation,
#       and I could probably make it much more effiecient by making Space
#       a subclass of Person, or vice-versa.
#       But, it's been so long since I wrote this that I do not want to mess
#       with it.

from math import floor
from random import randrange
import utils.ui as ui

# Declaration of Variables
SAT_THRESH = 0.7 #float(input("Satisfication Threshold: "))
OPEN_PERCENTAGE = 0.10

RED_PERCENTAGE = 0.85 - floor(OPEN_PERCENTAGE / 2) #float(input("Percentage of Reds: "))
BLUE_PERCENTAGE = 1 - RED_PERCENTAGE - (OPEN_PERCENTAGE - floor(OPEN_PERCENTAGE / 2))
GRID_SIZE = 30
CANVAS_SIZE = 700
PROJECT_NAME = "Social Simulation"

#Generation of board
display = ui.SquareField(CANVAS_SIZE, GRID_SIZE, PROJECT_NAME)
win = display.generate()

# Declaration of Person Class
class Person:
    def __init__(self, value, sat = None, x = None, y = None):
        self.sat = sat
        self.value = value
        self.color = "red" if value == -1 else "blue" if value == 1 else exit("Error: Person cannot have value other than 1 or -1")
        self.x = x
        self.y = y

    def getColor(self):
        return self.color

# Declaration of Emplty Space Class
class Space:
    def __init__(self, satBlue = None, satRed = None, x = None, y = None):
        self.value = 0
        self.satBlue = satBlue
        self.satRed = satRed
        self.color = "white"
        self.x = x
        self.y = y

    def getColor(self):
        return self.color
    
# Generation of Population
population = []

for i in range(round(GRID_SIZE * GRID_SIZE * RED_PERCENTAGE)):
    population.append(Person(-1))
for i in range(round(GRID_SIZE * GRID_SIZE * BLUE_PERCENTAGE)):
    population.append(Person(1))
for i in range(round(GRID_SIZE * GRID_SIZE * OPEN_PERCENTAGE)):
    population.append(Space())

# Generation of Locations
locations = []
for i in range(GRID_SIZE):
    tempArray = []
    for j in range(GRID_SIZE):
        num = randrange(0, len(population))
        currentSquare = population[num]
        currentSquare.x = j
        currentSquare.y = i
        tempArray.append(currentSquare)
        population.pop(num)
    locations.append(tempArray)

# Generation of Satisfaction
def getSatisfaction(value, x, y):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= y + i < GRID_SIZE and 0 <= x + j < GRID_SIZE  and (i != 0 or j != 0):
                neighbors.append(locations[y + i][x + j])
    
    similars = 0
    for neighbor in neighbors:
        if neighbor != None:
            if neighbor.value == value or neighbor.value == 0: similars += 1
    
    return similars / len(neighbors)


def generateSpaceSatisfication():
    for arr in locations:
        for lot in arr:
            if lot.value == 0:
                lot.satBlue = getSatisfaction(1, lot.x, lot.y)
                lot.satRed = getSatisfaction(-1, lot.x, lot.y)

generateSpaceSatisfication()           
display.update(locations)

win.getMouse()

# Warning: Heck of an algorithm incoming
change = True
while(change):
    change = False
    for i in range(len(locations)):
        for j in range(len(locations[i])):
            if locations[i][j].value != 0:
                locations[i][j].sat = getSatisfaction(locations[i][j].value, locations[i][j].x, locations[i][j].y)
                if locations[i][j].sat < SAT_THRESH:
                    generateSpaceSatisfication()
                    minSat = [0, 0, 0]
                    for k in range(len(locations)):
                        for l in range(len(locations[k])):
                            if locations[k][l].value == 0:
                                if (locations[k][l].satBlue if locations[i][j].value == 1 else locations[k][l].satRed) > minSat[0]:
                                    minSat = [locations[k][l].satBlue if locations[i][j].value == 1 else locations[k][l].satRed, k, l]
                    if minSat[0] > locations[i][j].sat:
                        tempx, tempy = locations[i][j].x, locations[i][j].y
                        locations[i][j].x, locations[i][j].y = locations[minSat[1]][minSat[2]].x, locations[minSat[1]][minSat[2]].y
                        locations[minSat[1]][minSat[2]].x, locations[minSat[1]][minSat[2]].y = tempx, tempy

                        temp = locations[i][j]
                        locations[i][j] = locations[minSat[1]][minSat[2]]
                        locations[minSat[1]][minSat[2]] = temp
                        
                        change = True
                        display.update(locations)

win.getMouse()
win.close()