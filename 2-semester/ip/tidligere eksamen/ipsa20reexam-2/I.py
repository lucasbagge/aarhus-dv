'''
    CALCULATOR CLASS

    In this problem you should create a class Calculator implementing a
    very simple calculator, storing an integer value. Calculator()
    should create a new Calculator object and initialize it to store
    the value 0.

    The class Calcuator should support the three methodds add, mult 
    and reset. Given a Calcuator c, the three methods should

      c.add(x)   # add x to the value stored in c
      c.mult(x)  # multiply the value stored in c by x
      c.reset()  # reset the value stored in c to 0

    Each of the three methods should return the new value stored in
    the Calculator c.

    An example usage of the class Calculator could be

      c = Calculator()
      print(c.add(7))
      print(c.mult(6))
      print(c.reset())
      print(c.add(1))
      print(c.add(2))
      print(c.add(3))

    that should print the values

      7
      42
      0
      1
      3
      6

    Input:  

      A Python expression using the Calculator class.

    Output: 

      The result of evaluation the expression.

    Example:

      Input:  [x for c in [Calculator()] for x in [c.add(7), c.mult(6), c.reset(), c.add(1), c.add(2), c.add(3)]]

      Output: [7, 42, 0, 1, 3, 6]

    Note:

      The below code already takes care of the input and output. 
      Your only task is to implement the methods in the
      class Calculator.
'''


class Calculator:
    pass  # insert code here


expression = input()
print(eval(expression))
