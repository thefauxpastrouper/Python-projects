import math
class Point:
    COUNT = 0
    def _init_(self, x, y):
        self.X = x
        self.Y = y
    def move(self, dx, dy):
        self.X = self.X + dx
        self.Y = self.Y + dy
    def _str_(self):
        return "Point(%s,%s)"%(self.X, self.Y)
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx*2 + dy*2)