class Point2D:
    __point_counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D.__point_counter += 1

    @property
    def get_point_counter(self):
        return self.__point_counter

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2) ** 0.5

point2D_1 = Point2D(5, 2)
point2D_2 = Point2D(3, 4)
print(Point2D.distance(point2D_1, point2D_2))

point3D_1 = Point3D(5, 2, 4)
point3D_2 = Point3D(3, 4, 5)
print(point3D_1.distance(point3D_2))

print(point2D_1.get_point_counter)

