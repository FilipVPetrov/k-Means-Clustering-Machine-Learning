import numpy as np

class Point(object):

    def __init__(self, x = 0.0, y = 0.0, color = ""):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return "Point [" + " x : " + str(self.x) + ", y : " + str(self.y) + " color: " + \
         str(self.color) + "]"

    @staticmethod
    def checkExistingPoint(currentPoint, listOfPoints):
        for point in listOfPoints:
            if point.x == currentPoint.x and point.y == currentPoint.y:
                return True
        return False

    @staticmethod
    def calculateDistance(first, second):
        return np.sqrt((first.x-second.x)**2 + (first.y-second.y)**2)