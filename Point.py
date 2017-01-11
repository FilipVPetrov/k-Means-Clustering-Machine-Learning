class Point(object):

    def __init__(self, x = 0.0, y = 0.0, color = ""):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return "Point [" + " x : " + str(self.x) + ", y : " + str(self.y) + " color: " + \
         str(self.color) + "]"