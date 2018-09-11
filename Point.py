"""
Name :Anirudh Mohan
Date :12/13/17

Description : Created a class with methods that contain respective objects and constructors, each having its own function.

"""


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.__x, self.__y)

    def __str__(self):
        return 'Point(x=%s, y=%s)' % (self.__x, self.__y)

    def dist_from_origin(self):
        length = (self.__x ** 2 + self.__y ** 2) ** 0.5
        print 'Distance to origin is = %s' % length

    def dist_from_point(self, other):
        dif_x = self.__x - other.__x
        dif_y = self.__y - other.__y
        length1 = (dif_x ** 2 + dif_y ** 2) ** 0.5
        print 'Distance between the points is = %s' % length1

# point1 = Point(7,7)
# point2 = Point(3,7)
# point3 = Point(2,5)
#
# point3.dist_from_origin()
# point3.dist_from_point(point2)
#
# print point3
# print point1 == point2
# print point1 == point3
