'''
    BROKEN FUNCTION
 
    In this problem you should write a function safe_evaluation(f, x),
    that returns f(x), provided the evaluation of f(x) does not cause
    an error. Otherwise, None should be returned.

    Input:

      The first line contains a Python lambda expression, representing
      a function f from floats to floats. The second line contains a
      Python list L of floats, with 1 <= len(L) <= 100.

    Output: 

      For each value x in L, print a line containing x and f(x)
      separated by a single space, both values should be printed in
      scientific notation with three decimals. If the evaluation of
      f(x) causes an error, instead x and None should be printed.

    Example:

      Input:  lambda x: 1.0 / x
              [-2.0, -1.0, 0.0, 1.0, 2.0]

      Output: -2.000e+00 -5.000e-01
              -1.000e+00 -1.000e+00
              0.000e+00 None
              1.000e+00 1.000e+00
              2.000e+00 5.000e-01

    Note: 

      The below code already implements the input and output for this
      problem. Your task is only to implement the function
      safe_evaluation.
'''


def safe_evaluation(f, x):
    pass  # insert code here
    

# solution
def safe_evaluation(f, x):
    try:
        return f(x)
    except:
        return None


f = eval(input())
L = eval(input())

assert 1 <= len(L) <= 100
assert all(isinstance(x, float) for x in L)

for x in L:
    y = safe_evaluation(f, x)
    print(f'{x:.3e}', f'{y:.3e}' if isinstance(y, float) else y)
