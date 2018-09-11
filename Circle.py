"""
Name :Anirudh Mohan
Date :12/13/17

Description : Created a class used to override some methods form Point and use it for its respective functions.

"""
from Point import Point


class Circle(Point):

    def __init__(self, x, y,  radius):
        Point.__init__(self, x, y)
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def __eq__(self, other):
        Point.__eq__(self, other)
        return self.get_x() == other.get_x() and self.get_y() == other.get_y() and self.__radius == other.__radius

    def __repr__(self):
        Point.__repr__(self)
        return 'Point(x=%s, y=%s) with radius = %s' % (self.get_x(), self.get_x(), self.__radius)

    def __str__(self):
        Point.__str__(self)
        return 'Point(x=%s, y=%s) with radius = %s' % (self.get_x(), self.get_x(), self.__radius)

    def area(self):
        area = self.__radius * self.__radius * 3.141592
        print 'Area of a circle is : %s' % area

    def circumference(self):
        circumference = 2 * self.__radius * 3.141592
        print 'Circumference of a circle is : %s' % circumference

    def edge_dist_from_origin(self):
        length = (self.get_x() ** 2 + self.get_y() ** 2) ** 0.5
        distance = length - self.__radius
        print 'Distance from the edge of the circle to Origin : %s' % distance

    def circle_intersect_with(self, other):
        dif_x = self.get_x() - other.get_x()
        dif_y = self.get_y() - other.get_y()
        add_r = self.__radius + other.__radius
        sub_r = self.__radius - other.__radius
        length1 = (dif_x ** 2 + dif_y ** 2) ** 0.5
        if length1 > sub_r and length1 < add_r:
            print 'Circles Intersect'
        else:
            print 'No Circles Intersect'



# point1 = Circle(7, 7, 5)
# point2 = Circle(7, 7, 1)
# point3 = Circle(0, 6, 4)
# point4 = Circle(5, 5, 4)
#
# print point1 == point2
# print point2
#
# point1.area()
# point1.circumference()
# point1.edge_dist_from_origin()
# point3.circle_intersect_with(point4)
