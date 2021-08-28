class Quadrilateral:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def draw(self):
        top = '*'
        w = 0
        while w < ((self.x3 - self.x1) - 2):
            top = top + '*'
            w = w + 1
        top = top + '*'
        print(top)

        h = 0
        while h < ((self.y3 - self.y1) - 2):
            line = '*'
            w = 0
            while w < ((self.x3 - self.x1) - 2):
                line = line + ' '
                w = w + 1
            line = line + '*'
            print(line)
            h = h + 1

        top = '*'
        w = 0
        while w < ((self.x3 - self.x1) - 2):
            top = top + '*'
            w = w + 1
        top = top + '*'
        print(top)


class Rectangle(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)
        self.length = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** (1/2)
        self.width = ((x1 - x4) * (x1 - x4) + (y1 - y4) * (y1 - y4)) ** (1/2)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


class Square(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)
        self.side = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** (1/2)

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

s = Square(0, 0, 10, 0, 10, 10, 0, 10)
print("Square area: " + str(s.area()))
print("Square perimeter: " + str(s.perimeter()))
s.draw()

r = Rectangle(0, 0, 7, 0, 7, 5, 0, 5)
print("Rectangle area: " + str(r.area()))
print("Rectangle perimeter: " + str(r.perimeter()))
r.draw()
