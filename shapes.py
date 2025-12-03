from sac_graphics import *


class Lshape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.shapes = []
        self.__create_shape()
        self.type = 'Lshape'

    def __create_shape(self):
        pt1 = Point(self.x, self.y)
        pt2 = Point(self.x + 25, self.y + 25)
        for i in range(4):
            self.shapes.append(Rectangle(pt1, pt2))
            pt1 = Point(pt1.getX(), pt1.getY() + 25)
            pt2 = Point(pt2.getX(), pt2.getY() + 25)
        pt1 = Point(pt1.getX() + 25, pt1.getY() - 25)
        pt2 = Point(pt2.getX() + 25, pt2.getY() - 25)
        self.shapes.append(Rectangle(pt1, pt2))
        for shape in self.shapes:
            shape.setFill(self.color)

    def draw(self, win):
        for shape in self.shapes:
            shape.draw(win)

    def undraw(self):
        for shape in self.shapes:
            shape.undraw()


class Vline:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.shapes = []
        self.__create_shape()
        self.type = 'Vline'

    def __create_shape(self):
        pt1 = Point(self.x, self.y)
        pt2 = Point(self.x + 25, self.y + 25)
        for i in range(4):
            self.shapes.append(Rectangle(pt1, pt2))
            pt1 = Point(pt1.getX(), pt1.getY() + 25)
            pt2 = Point(pt2.getX(), pt2.getY() + 25)
        self.shapes.append(Rectangle(pt1, pt2))
        for shape in self.shapes:
            shape.setFill(self.color)

    def draw(self, win):
        for shape in self.shapes:
            shape.draw(win)

    def undraw(self):
        for shape in self.shapes:
            shape.undraw()


class Hline:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.shapes = []
        self.__create_shape()
        self.type = 'Hline'

    def __create_shape(self):
        pt1 = Point(self.x, self.y)
        pt2 = Point(self.x + 25, self.y + 25)
        for i in range(4):
            self.shapes.append(Rectangle(pt1, pt2))
            pt1 = Point(pt1.getX() + 25, pt1.getY())
            pt2 = Point(pt2.getX() + 25, pt2.getY())
        self.shapes.append(Rectangle(pt1, pt2))
        for shape in self.shapes:
            shape.setFill(self.color)

    def draw(self, win):
        for shape in self.shapes:
            shape.draw(win)

    def undraw(self):
        for shape in self.shapes:
            shape.undraw()


class SingleCube:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.shapes = []
        self.__create_shape()
        self.type = 'SingleCube'

    def __create_shape(self):
        pt1 = Point(self.x, self.y)
        pt2 = Point(self.x + 25, self.y + 25)
        self.shapes.append(Rectangle(pt1, pt2))
        for shape in self.shapes:
            shape.setFill(self.color)

    def draw(self, win):
        for shape in self.shapes:
            shape.draw(win)

    def undraw(self):
        for shape in self.shapes:
            shape.undraw()


class Bcube:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.shapes = []
        self.__create_shape()
        self.type = 'Bcube'

    def __create_shape(self):
        pt1 = Point(self.x, self.y)
        pt2 = Point(self.x + 25, self.y + 25)
        self.shapes.append(Rectangle(pt1, pt2))
        pt1 = Point(pt1.getX() + 25, pt1.getY())
        pt2 = Point(pt2.getX() + 25, pt2.getY())
        self.shapes.append(Rectangle(pt1, pt2))
        pt1 = Point(pt1.getX(), pt1.getY() + 25)
        pt2 = Point(pt2.getX(), pt2.getY() + 25)
        self.shapes.append(Rectangle(pt1, pt2))
        pt1 = Point(pt1.getX() - 25, pt1.getY())
        pt2 = Point(pt2.getX() - 25, pt2.getY())
        self.shapes.append(Rectangle(pt1, pt2))
        for shape in self.shapes:
            shape.setFill(self.color)

    def draw(self, win):
        for shape in self.shapes:
            shape.draw(win)

    def undraw(self):
        for shape in self.shapes:
            shape.undraw()
