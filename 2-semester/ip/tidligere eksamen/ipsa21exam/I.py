'''
    ROTATING VECTOR

    Your task is to create a class Vector to represent two-dimensional vectors.
    An object v of class Vector should be created by v = Vector(x, y),
    where x and y are floats. Create methods mult and rotate: 
    v.mult(c) should scale the x and y coordinates by the float c, and
    v.rotate() should rotate the vector 90 degrees counter clockwise.
    Both mult and rotate should change the vector and return None.
    Finally, define __str__ (used by str and print) to return the string
    'Vector(x, y)', where the x and y coordinates are shown with 3 decimals.

    Example of usage:
    
        > v = Vector(1.0, 3.0)
        > print(v)
        Vector(1.000, 3.000)
        > v.rotate()
        > print(v)
        Vector(-3.000, 1.000)
        > v.mult(0.5)
        > print(v)
        Vector(-1.500, 0.500)

    Input:  A Python expression using the class Vector.

    Output: The output generated by evaluating the input expression.

    Example:

      Input:  print(*[x for v in [Vector(2.0, 1.0)] for x in [str(v), v.rotate(), v.mult(1 / 3), str(v)]])
    
      Output: Vector(2.000, 1.000) None None Vector(-0.333, 0.667)
 
    Note: The below code already takes care of handling the input and output.
'''


class Vector:

    def __init__(self, x, y):

        self.x = x

        self.y = y

        self.vector = [x, y]



    def rotate(self):

        return Vector(-1 * self.y, self.x)



    def mult(self, factor):

        return Vector(self.x * factor, self.y * factor)

        

    def __str__(self):

        return (f'Vector({self.x:.3f}, {self.y:.3f})')
    
eval(input())