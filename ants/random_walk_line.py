from graphics import *
from random import randint
from math import sqrt
from wave_to_RGB import wave_to_RGB

x, y = (714, 714)
centerPoint = [x/2, y/2]
squareLength = 5

win = GraphWin("Random Walk", x, y)

def generatePoints(arr, squareLength = squareLength):
    centerX, centerY = arr
    p1 = Point(centerX - squareLength, centerY - squareLength)
    p2 = Point(centerX + squareLength, centerY + squareLength)
    return p1, p2

def testPoint(point):
    if(point + squareLength > x or point - squareLength < 0):
        return False
    else: return True

def getColorFromDistance(version, currentCenter):
    currentCenter = [currentCenter.getX(), currentCenter.getY()]
    distance = currentCenter[0]
    print(version, distance / 2)
    rgb = wave_to_RGB(distance / 2 + 380)
    return color_rgb(rgb[0], rgb[1], rgb[2])

class Ant:
    count = 0

    def __init__(self, centerPoint):
        self.version = Ant.count
        Ant.count += 1
        self.centerPoint = centerPoint
        self.cornerPoints = generatePoints(self.centerPoint)
        self.ant = Rectangle(self.cornerPoints[0], self.cornerPoints[1])
        self.color = getColorFromDistance(self.version, Point(self.centerPoint[0], self.centerPoint[1]))
        self.ant.setFill(self.color)
        self.ant.draw(win)

def move(ant):
    num = randint(0, 3)
    centerPoint = ant.centerPoint

    if(num == 0):
        #North
        if(testPoint(centerPoint[1] + (squareLength * 2))):
            centerPoint[1] = centerPoint[1] + (squareLength * 2)
    elif(num == 1):
        #East
        if(testPoint(centerPoint[0] + (squareLength * 2))):
            centerPoint[0] = centerPoint[0] + (squareLength * 2)
    elif(num == 2):
        #South
        if(testPoint(centerPoint[1] - (squareLength * 2))):
            centerPoint[1] = centerPoint[1] - (squareLength * 2)
    elif(num == 3):
        #West
        if(testPoint(centerPoint[0] - (squareLength * 2))):
            centerPoint[0] = centerPoint[0] - (squareLength * 2)
    else:
        exit("Error, out of random range")

    ant.ant.setOutline(ant.color)
    return Ant(centerPoint)

ants = []
for i in range(0, 10):
    ants.append(Ant([x/2, y/2]))

while True:
    for i in range(len(ants)):
        ants[i] = move(ants[i])

win.getMouse()
win.close()