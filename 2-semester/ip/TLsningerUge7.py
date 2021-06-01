# Exercise 11.1 (PersonReader)
class PersonReader:
    def __init__(self):
        self.name = None
        self.year = None

    def input(self):
        self.name = input('name: ')
        self.year = input('year: ')

    def __str__(self):
        return f'{self.name},{self.year}'


# Exercise 11.2 (Stopwatch)
from time import time


class Stopwatch:
    def __init__(self):
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time()
            self.laps = []

    def stop(self):
        self.end_time = time()
        self.running = False

    def lap(self):
        self.laps.append(time())

    def total_time(self):
        if self.running:
            end = time()
        else:
            end = self.end_time
        return end - self.start_time

    def lap_times(self):
        if self.running:
            end = time()
        else:
            end = self.end_time
        return [end - start for end, start in
                zip(self.laps + [end], [self.start_time] + self.laps)]


# Exercise 11.3 (2D vector)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vector = [x, y]

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def add(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    # __add__ = add

    def __add__(self, other_vector):
        #    return self.add(other_vector)
        return [[(x + a, y + b)] for (x, y) in self.vector for (a, b) in
                other_vector.vector]

    def mult(self, factor):
        return Vector(self.x * factor, self.y * factor)

    def dot(self, vector):
        return Vector(self.x * vector.x, self.y * vector.y)

    def __mul__(self, other):
        if isinstance(other, (tuple, Vector)):
            return self.dot(other)
        else:
            return self.mult(other)

    def __rmul__(self, other):
        return self.mult(other)

    def __str__(self):
        return f"<{self.x}, {self.y}>"


# Exercise 12.1 (geometric shapes)
from math import pi


class Shape:
    def fatness(self):
        if self.perimeter:
            return 4 * pi * self.area() / self.perimeter() ** 2
        else:
            return 0


class Circle(Shape):
    def __init__(self, radius, center_x, center_y):
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y

    def __str__(self):
        return f'Circle(radius={self.radius}, center=({self.center_x},{self.center_y}))'

    def area(self):
        return self.radius ** 2 * pi

    def perimeter(self):
        return 2 * pi * self.radius

    def contains(self, x, y):
        return ((self.center_x - x) ** 2 + (
                    self.center_y - y) ** 2) ** 0.5 <= self.radius


class Rectangle(Shape):
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def __str__(self):
        return f'Rectangle(({self.min_x},{self.min_y}),({self.max_x},{self.max_y}))'

    def area(self):
        return (self.max_x - self.min_x) * (self.max_y - self.min_y)

    def perimeter(self):
        return (self.max_x - self.min_x) * 2 + (self.max_y - self.min_y) * 2

    def contains(self, x, y):
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y


class Triangle(Shape):
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.x0, self.y0, self.x1, self.y1, self.x2, self.y2 = x0, y0, x1, y1, x2, y2

    def __str__(self):
        return f'Triangle(({self.x0}, {self.y0}),({self.x1},{self.y1}),({self.x2},{self.y2}))'

    def area(self):
        return abs((self.x0 - self.x2) * (self.y1 - self.y0)
                   - (self.x0 - self.x1) * (self.y2 - self.y0)) / 2

    def perimeter(self):
        def dist(x0, y0, x1, y1):
            return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

        return (dist(self.x0, self.y0, self.x1, self.y1) +
                dist(self.x1, self.y1, self.x2, self.y2) +
                dist(self.x0, self.y0, self.x2, self.y2))

    def contains(self, x, y):
        A = Triangle(self.x0, self.y0, self.x1, self.y1, self.x2,
                     self.y2).area()

        A1 = Triangle(x, y, self.x1, self.y1, self.x2, self.y2).area()

        A2 = Triangle(self.x0, self.y0, x, y, self.x2, self.y2).area()

        A3 = Triangle(self.x0, self.y0, self.x1, self.y1, x, y).area()

        return A == A1 + A2 + A3

# live session

class MinEx(Exception):
    pass

def create_pairs(X,Y):
    L = []
    for i in range(len(X)):
        L.append((X[i], Y[i]))
    return L

def create_pairss(X,Y):
    if len(X) != len(Y):
        raise  MinEx ('Stop')
    return list(zip(X,Y))

print(create_pairss([1,2,3], [4,5]))

try: 
    print(create_pairss([1,2,3], [4,5]))
except Exception:
    print('Jeg er dum')
    
filename = '2-semester/ip/cano.txt'

file = open(filename)
lines = file.readlines()
file.close()

for line in lines:
    if 'mathematical' in line.lower():
        print(line, end = '')
        
with open(filename) as file:
    for line in lines:
        if 'mathematical' in line.lower():
            print(line, end = '')
savename = "2-semester/ip/selected_line.txt"

with open(filename) as file:
    with open(savename, 'w') as savefile:
            for line in lines:
                if 'mathematical' in line.lower():
                    #print(line, file = savefile, end = '')
                    savefile.write(line)

