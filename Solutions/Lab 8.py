from math import *
#   Parent Class 1 --> Rectangle
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area_rect(self):
        return self.width * self.height

    def get_perimeter_rect(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return '\n' + 'Width=' + str(self.width) + '\n' + 'Height=' + str(self.height) + '\n' + 'Area=' + str("{:.2f}".format(self.get_area_rect())) + '\n' + 'Perimeter=' + str("{:.2f}".format(self.get_perimeter_rect()))


#   Parent Class 2 --> Triangle
class Triangle:

    def __init__(self, edge):
        self.edge = edge

    def get_area_tr(self):
        return (self.edge ** 2) * sqrt(3)/4

    def get_perimeter_tr(self):
        return 3 * self.edge

    def __str__(self):
        return '\n' + 'Edge=' + str(self.edge) + '\n' + 'Area=' + str("{0:.2f}".format(self.get_area_tr())) + '\n' + 'Perimeter=' + str("{0:.2f}".format(self.get_perimeter_tr()))


#   Child Class 1 --> Square
class Square(Rectangle):

    def __init__(self, edge):
        self.width = edge
        self.height = edge

    def __str__(self):
        return super(Square, self).__str__()

#   Child Class 2 --> SquarePyramid
class SquarePyramid(Square, Triangle):

    def __init__(self, edge):
        self.edge = edge
        self.width = edge
        self.height = edge

    def get_area(self):
        return Square.get_area_rect(self) + 3 * Triangle.get_area_tr(self)

    def __str__(self):
        return '\n' + 'Area=' + str("{0:.2f}".format(self.get_area()))


#   Child Class 3 --> TrianglePrism
class TrianglePrism(Rectangle, Triangle):

    def __init__(self, edge, height):
        self.edge = edge
        self.height = height
        self.width = edge

    def get_volume(self):
        return (Triangle.get_area_tr(self)) * self.height

    def get_area(self):
        return 2 * (Triangle.get_area_tr(self)) + 3 * (Rectangle.get_area_rect(self))

    def __str__(self):
        return '\n' + 'Area=' + str("{0:.2f}".format(self.get_area())) + '\n' + 'Volume=' + str("{0:.2f}".format(self.get_volume()))
