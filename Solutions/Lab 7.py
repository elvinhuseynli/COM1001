from math import *
#  Parent class  ---->  Shape


class Shape:

    def __init__(self, name, color, line_type, thickness):
        self.name = name
        self.color = color
        self.line_type = line_type
        self.thickness = thickness

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
        return self.name

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_line_type(self):
        return self.line_type

    def set_line_type(self, new_line_type):
        self.line_type = new_line_type

    def get_thickness(self):
        return self.thickness

    def set_thickness(self, new_thickness):
        self.thickness = new_thickness

    def __str__(self):
        return "Name=" + self.name + "\n" + "Color=" + self.color + "\n" + "Line type=" + self.line_type + "\n" + "Thickness=" + str(self.thickness)


#   Child Class No-1 ----> Rectangle
class Rectangle(Shape):

    def __init__(self, width, height, *args, **kwargs):
        self.width = width
        self.height = height
        super(Rectangle, self).__init__(*args, **kwargs)

    def get_width(self):
        return self.width

    def set_width(self, new_width):
        self.width = new_width

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        print(super(Rectangle, self).__str__())
        return "Width=" + str(self.width) + "\n" + "Height=" + str(self.height) + "\n" + "Area=" + str("{:.2f}".format(self.width * self.height)) + "\n" + "Perimeter=" + str("{:.2f}".format(2 * (self.width + self.height)))


#   Child Class No-2 ----> Circle
class Circle(Shape):

    def __init__(self, radius, *args, **kwargs):
        self.radius = radius
        super(Circle, self).__init__(*args, **kwargs)

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        print(super(Circle, self).__str__())
        return "Radius=" + str(self.radius) + "\n" + "Area=" + str("{:.2f}".format(pi * (self.radius ** 2))) + "\n" + "Perimeter=" + str("{:.2f}".format(2 * pi *self.radius))


#   Child Class No-3 ----> Triangle
class Triangle(Shape):

    def __init__(self, edge1, edge2, edge3, *args, **kwargs):
        self.edge1 = edge1
        self.edge2 = edge2
        self.edge3 = edge3
        super(Triangle, self).__init__(*args, **kwargs)

    def get_edge1(self):
        return self.edge1

    def set_edge1(self, new_edge1):
        self.edge1 = new_edge1

    def get_edge2(self):
        return self.edge2

    def set_edge2(self, new_edge2):
        self.edge2 = new_edge2

    def get_edge3(self):
        return self.edge3

    def set_edge3(self, new_edge3):
        self.edge3 = new_edge3

    def get_area(self):
        u = (self.edge1 + self.edge2 + self.edge3) / 2
        return str(float(sqrt(u * (u - self.edge1) * (u - self.edge2) * (u - self.edge3))))

    def get_perimeter(self):
        return str(float(self.edge1 + self.edge2 + self.edge3))
    
    def __str__(self):
        print(super(Triangle, self).__str__())
        a = (self.edge1 + self.edge2 + self.edge3) / 2
        return "Edge1=" + str(self.edge1) + "\n" + "Edge2=" + str(self.edge2) + "\n" + "Edge3=" + str(self.edge3) + "\n" + "Area=" + str("{:.2f}".format(sqrt(a * (a - self.edge1) * (a - self.edge2) * (a - self.edge3)))) + "\n" + "Perimeter=" + str("{:.2f}".format(a * 2))


#   Child Class No-4 ----> Square
class Square(Shape):

    def __init__(self, edge, *args, **kwargs):
        self.edge = edge
        super(Square, self).__init__(*args, **kwargs)

    def get_edge(self):
        return self.edge

    def set_edge(self, new_edge):
        self.edge = new_edge

    def get_area(self):
        return self.edge ** 2

    def get_perimeter(self):
        return 4 * self.edge

    def __str__(self):
        print(super(Square, self).__str__())
        return "Edge=" + str(self.edge) + "\n" + "Area=" + str("{:.2f}".format(self.edge ** 2)) + "\n" + "Perimeter=" + str("{:.2f}".format(4 * self.edge))
