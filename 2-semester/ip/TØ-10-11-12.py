# 11.3 
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    def add(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __add__(self, other):
        return self.add(other)

    def mult(self, vector):
        return Vector(self.x * factor, self.y * factor)

    def dot(self, vector):
        return self.x * vector.x + self.y * vector.y

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return self.mult(other)

    def __rmul__(self, other):
        return self.mult(other)

    def __str__(self):
        return "<%s, %s>" % (self.x, self.y)

vec1 = Vector(4,5)
vec2 = Vector(1,1)
vec1.dot(vec2)
print(vec1.length())
print(vec1.add(vec2))
print(vec2 + vec1)
print(vec1.mult(3))
print(vec1.dot(vec2))
print(vec1 * vec2)

# 12.1
import numpy as np
class Shape:
    def fatness(self):
        return 4 * np.pi * self.area() / self.perimeter() ** 2

class Circle(Shape):
    def __init__(self, radius, center_x, center_y):
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y

    def __str__(self):
        return f'Circle(radius = {self.radius}, center = ({self.center_x}, {self.center_y})'

    def area(self):
        return np.pi * self.radius ** 2

    def parimeter(self):
        return np.pi * self.radius * 2

    def contains(self, x, y):
        return (x - self.center_x) ** 2 + (y - self.center_y) ** 2 < self.radius **2

class Ractangle(Shape):

    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.min_y = min_y
        self.a = self.max_x - self.min_x
        self.b = self.max_y - self.min_y

    def __str__(self):
        return f'Ractangle(min:({self.min_x}, {self.min_y}), max:({self.max_x},{self.max_y}))'

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2*self.a + 2*self.b

    def contains(self, x, y):
         return self.min_x < x < self.max_x and self.min_y < y < self.max_y

class Triangle(Shape):
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f'Triangle(({self.x0}, {self.y0}), {self.x1}, {self.y1}, ({self.x2},{self.y2}))'


    def area(self):
        p0 = self.x0 * (self.y1 - self.y2)
        p1 = self.x1 * (self.y2 - self.y0)
        p2 = self.x2 * (self.y0 - self.y1)
        return abs((p0 + p1 + p2) / 2)

    def perimeter(self):
        k0 = np.sqrt((self.x0 - self.x1) ** 2 + (self.y0 - self.y1) ** 2)
        k1 = np.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        k2 = np.sqrt((self.x0 - self.x2) ** 2 + (self.y0 - self.y2) ** 2)
        return k0 + k1 + k2

    def contains(self, x, y) 
         a0 = x * (self.y1 - self.y2) 
         a1 = self.x1 * (self.y2 - y) 
         a2 = self.c2 * (y - self.y1) 
         A = abs((a0 + a1 +a2)/2)

         b0 = self.x0 * (y - self.y2)
         b1 = x * (self.y2 - self.y0)
         b2 = self.x2 + (self.y0 - y)
         B = abs((b0 + b1 + b2)/2)

         c0 = self.x0 * (self.y1 - y) 
         c1 = self.x1 * (y - self.y0) 
         c2 = x * (self.y0 - self.y1) 
         C = abs((c0 + c1 + c2)/2)
        
        return (A+B+C) == self.area()






