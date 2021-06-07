'''
    INTERPOLATE

    Your task is to create a decorator 'interpolate'.  Assume you have
    a function f that is only defined on integers.  By applying the
    decorator @interpolate to f, the function should now be defined on
    floats, and for a float x, where i <= x < i + 1, for some integer i, 
    the function should return the linear interpolated value between 
    f(i) and f(i + 1). Example:

        @interpolate
        def f(x):
            return x ** 2 if isinstance(x, int) else None

    should return f(2.0) = 4.0,  f(3.0) = 9.0, and f(2.5) = 6.5.

    Note:

        The below input-output is already handled by the code provided.
        Your only task is to define the decorator 'interpolate'.

    Input:

        The first line contains a python expression, applying your
        decorator 'interpolate' to a lambda expression, that is a
        function on integers.  The second line contains a Python list L
        containing floats, where len(L) <= 100.

    Output:

        For each value x in the list L, print a line with x and f(x)
        separated by space. Both values should be printed as floats with
        three decimals.

    Example:

      Input:  interpolate(lambda x: x ** 2 if isinstance(x, int) else None)
              [-3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]

      Output: -3.000 9.000
              -2.500 6.500
              -2.000 4.000
              -1.500 2.500
              -1.000 1.000
              -0.500 0.500
              0.000 0.000
              0.500 0.500
              1.000 1.000
              1.500 2.500
              2.000 4.000
              2.500 6.500
              3.000 9.000
'''


import math

def interpolate(f):
    def wrapper(x):
        i = math.floor(x)
        alpha = x - i
        return (1 - alpha) * f(i) + alpha * f(i + 1)

    return wrapper


interpolated_function = eval(input())
L = eval(input())

assert len(L) <= 100 and all(isinstance(x, float) for x in L)

for x in L:
    print(f'{x:.3f} {interpolated_function(x):.3f}')
