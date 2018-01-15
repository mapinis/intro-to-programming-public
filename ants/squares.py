from math import floor, sqrt
from graphics import *
from wave_to_RGB import wave_to_RGB

squareLength = int(input("Square half length: "))
side = 750
centerPoint = [side / 2, side / 2]
win = GraphWin("Square Test", side, side)

def generatePoints(arr, squareLength = squareLength):
    centerX, centerY = arr
    p1 = Point(centerX - squareLength, centerY - squareLength)
    p2 = Point(centerX + squareLength, centerY + squareLength)
    return p1, p2

def getColorFromDistance(currentCenter):
    distance = sqrt(((currentCenter[0] - centerPoint[0]) ** 2) + ((currentCenter[1] - centerPoint[1]) ** 2))
    #distance = currentCenter[0]
    rgb = wave_to_RGB(distance / 2 + 380)
    return color_rgb(rgb[0], rgb[1], rgb[2])

length = 1
while(True):
    length += 2
    points = [[-floor(length/2), floor(length/2)]]
    for i in range(1, length):
        points.append([points[-i][0] + i, points[-i][1]])
    for i in range(1, length):
        points.append([points[-i][0], points[-i][1] - i])
    for i in range(1, length):
        points.append([points[-i][0] - i, points[-i][1]])
    for i in range(1, length):
        points.append([points[-i][0], points[-i][1] + i])
    
    points = list(map(lambda arr: [centerPoint[0] + (arr[0] * squareLength), 
                centerPoint[1] + (arr[1] * squareLength)], points))
    for point in points:
        if(point[0] <= side or point[1] <= side):
            cornerPoints = generatePoints(point)
            square = Rectangle(cornerPoints[0], cornerPoints[1])
            color = getColorFromDistance(point)
            square.setFill(color)
            square.setOutline(color)
            square.draw(win)
        else:
            break
    else:
        continue
    break

win.getMouse()
win.close()