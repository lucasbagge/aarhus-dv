'''
    SMOOTH

    Your task is to create a decorator 'smooth', that should take a
    function f defined on integers, and return a new function g:

        g(x) :=   0.10 * f(x - 2)
                + 0.25 * f(x - 1)
                + 0.30 * f(x)
                + 0.25 * f(x + 1)
                + 0.10 * f(x + 2)
    
    If we apply the decorator smooth as follows

        @smooth
        def f(x):
            return abs(x)

    then f(1) = 1.2, since 0.1 * abs(1 - 2) + 0.25 * abs(1 - 1) 
    + 0.3 * abs(1) + 0.25 * abs(1 + 1) + 0.1 * abs(1 + 2) = 1.2.

    Input:  Two lines. The first line is a Python expression 
            using the decorator smooth, to create a function f.
            The second line is a Python list L of integers, where
            1 <= len(L) <= 100.

    Output: For each integer x in L, the output contains a line with x
            and f(x), separated by space. The result f(x) should be
            printed using 3 decimals.

    Example:

      Input:  smooth(lambda x: abs(x))
              [-3, -2, -1, 0, 1, 2, 3]

      Output: -3 3.000
              -2 2.000
              -1 1.200
              0 0.900
              1 1.200
              2 2.000
              3 3.000

    Note: 

      The below code already handles the input and ouput. 
      Your task is only to create the decorator smooth.
'''


def smooth(f):
    pass  # insert code here


smoothed_function = eval(input())
L = eval(input())
for x in L:
    y = smoothed_function(x)
    print(x, f'{y:.3f}')

