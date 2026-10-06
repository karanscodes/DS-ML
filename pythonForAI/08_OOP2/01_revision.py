class Point:

    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y
    
    def __str__(self):
        return f"({self.x_cod},{self.y_cod})"

    def euclidean_distance(self, other):
        x1 = self.x_cod
        x2 = other.x_cod
        y1 = self.y_cod
        y2 = other.y_cod
    
        return ((x1-x2)**2 + (y1-y2)**2)**0.5
    
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))


class Line:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f"{self.a}x + {self.b}y + {self.c} = 0"

    def point_on_line(line, point):
        if line.a * point.x_cod + line.b * point.y_cod + line.c == 0:
            return "Lies on the Line"
        else:
            return "Does NOT Lie on the Line"

    def shortest_distance(line, point):
        return abs(line.a * point.x_cod + line.b * point.y_cod + line.c)/(line.a**2 + line.b**2)**0.5


one = Point(2,3)
print(one)

B = Point(0,2)
C = Point(0,3)
print(B.euclidean_distance(C))
print(B.distance_from_origin())


# Line Object 
line1 = Line(3,4,5)
print(line1)

line2 = Line(1,1,-2)
point2 = Point(1,1)

print(line2, point2)
print(line2.point_on_line(point2))


line3 = Line(3,-1,-10)
point3 = Point(-4,2)

print(line3.shortest_distance(point3))