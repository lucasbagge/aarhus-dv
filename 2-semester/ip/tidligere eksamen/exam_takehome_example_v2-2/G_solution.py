'''CLASSES FOR GEOMETRIC SHAPES

   In this exercise we consider the representation of three geometric
   shapes with a closed perimeter defined by a list of points - polygons,
   rectangles and triangles. Rectangles and triangles are just special
   types of polygons defined by 4 and 3 points, respectively. We
   consider each of the three shapes as defined by a class: Polygon,
   Rectangle and Triangle.  Rectangle and Triangle are subclasses of
   Polygon. YOUR TASK IS TO CREATE THE __init__ METHODS FOR THE CLASSES
   Rectangle and Triangle, AND NO OTHER METHOD.

   Below is provided the code for the class Polygon. A polygon object
   is created by providing the list of (x, y) points on the
   perimeter as an argument to the __init__ method, e.g.

     polygon = Polygon([(-1, -1), (2, 3), (1, 1), (3, 2)])

   The length of the perimeter and the area of a polygon object, are computed
   using:

     polygon.length()  # returns 14.472 
     polygon.area()    # returns 2.000

   You should implement the __init__ methods of both classes (and no
   other method!), such that a rectangle can be created by

     rectangle = Rectangle(width, height)

   and a triangle by

     triangle = Triangle(a, b, c)

   For a rectangle the four points defining the rectangle should be:
         (0,0), (0, height), (width, height), (width, 0)

   For a triangle you are free to select the three points, as long they
   form a triangle with side lengths a, b and c.
   
   The below test program reads from input first an integer n, followed
   by n lines containing one of the three shapes:

      Polygon(list_of_points)
      Rectangle(width, height)
      Triangle(a, b, c)

   For each shape in the input the length of the perimeter and area are
   printed with 3 decimals.
'''

from math import sqrt

class Polygon:
    '''Class to represent polygon objects.'''

    def __init__(self, points):
        '''Initialize a Polygon object with a list of points.'''
        
        self.points = points

    def length(self):
        '''Return the length of the perimeter of the polygon.'''

        P = self.points
        
        return sum(sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
                   for (x0, y0), (x1, y1) in zip(P, P[1:] + P[:1]))

    def area(self):
        '''Return the area of the polygon.'''
        
        P = self.points
        A = 0
        for (x0, y0), (x1, y1) in zip(P, P[1:] + P[:1]):
            A += x0 * y1 - y0 * x1
        return abs(A / 2)


class Rectangle(Polygon):

#   vvvvvvvvvvvvv   insert code for __init__ below   vvvvvvvvvvvvvv

    pass

    def __init__(self, width, height):
        self.points = [(0,0), (0, height), (width, height), (width, 0)]

#   ^^^^^^^^^^^^^^^^^^^^^^   end of insert   ^^^^^^^^^^^^^^^^^^^^^^


class Triangle(Polygon):

#   vvvvvvvvvvvvv   insert code for __init__ below   vvvvvvvvvvvvvv

    pass

    def __init__(self, a, b, c):
        x = (a** 2 + b ** 2 - c ** 2) / (2 * a)
        y = sqrt(b ** 2 - x ** 2)
        self.points = [(0, 0), (a, 0), (x, y)]

#   ^^^^^^^^^^^^^^^^^^^^^^   end of insert   ^^^^^^^^^^^^^^^^^^^^^^


# Test code: Read input shapes and print their length and area

number_of_shapes = int(input())

for _ in range(number_of_shapes):
    shape = eval(input())
    length = shape.length()
    area = shape.area()
    print(f'{length:.3f} {area:.3f}')
