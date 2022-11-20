import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point):
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        return math.sqrt(dx ** 2 + dy ** 2)


class Rectangle:
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def area(self):
        lungime = distance(self.p1, self.p2) #260
        latime = distance(self.p1, self.p3)
        return lungime * latime

b2=Rectangle((16,34), (8, 20), (47, 16), (39, 2))
print(b2)

print((math.sqrt(8 ** 2 + 14 ** 2)*(math.sqrt((-31) ** 2 + (18) ** 2))))
print(math.sqrt((-31) ** 2 + (18) ** 2))