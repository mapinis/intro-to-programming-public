########################
# Name: Mark Apinis
# Date: May 25, 2017
# File: ui.py
# Description: A module in order to generate GUIs based on graphics.py
########################

from utils.graphics import *

class SquareField:

    def __init__(self, canvasSize, gridSize, projectName):
        self._canvasSize = canvasSize # Canvas size, in pixels
        self._squareHalfLength = int(canvasSize / gridSize / 2) # Half of the length of each square
        self._gridSize = gridSize # Grid size
        self._drawnSquares = [] # Array of all the squares objects
        self._win = None # The graphics object
        self._projectName = projectName # The name that should appear at the top of the graphics

    # Generates the corner points of a square based on its center points and half length
    def generatePoints(self, center):
        centerX, centerY = center
        p1 = Point(centerX - self._squareHalfLength, centerY - self._squareHalfLength)
        p2 = Point(centerX + self._squareHalfLength, centerY + self._squareHalfLength)
        return p1, p2

    # Generates the graphics object, returns it, and the field
    def generate(self):
        self._win = GraphWin(self._projectName, self._canvasSize, self._canvasSize)

        for i in range(self._gridSize):
            tempArray = [] # Creates an array for each row on thefield
            for j in range(self._gridSize):
                cornerPoints = self.generatePoints((j * self._squareHalfLength * 2 + self._squareHalfLength, i * self._squareHalfLength * 2 + self._squareHalfLength))
                square = Rectangle(cornerPoints[0], cornerPoints[1]) # Creates the square object
                square.setFill("black") # Sets the temporary color
                square.setOutline("black") # Sets the permanent outline color
                square.draw(self._win) # Places on field
                tempArray.append(square)
            self._drawnSquares.append(tempArray)

        return self._win # Returns it to the main program so that things like win.getMouse() can be called

    # Gets the color of the objects in the given array and assigns colors to the field accordingly
    def update(self, inList):
        for i in range(self._gridSize):
            for j in range(self._gridSize):
                self._drawnSquares[i][j].setFill(inList[i][j].getColor()) # Pretty self-explanatory