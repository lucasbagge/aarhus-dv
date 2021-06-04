'''
    SQUARES

    In this task you should write a function squares(numbers), that
    given a sorted list of distinct positive integers numbers, 
    returns a sorted list of all i where i ** 2 is in numbers.

    Input:  

      A single line containing a Python list, numbers, containing
      distinct positive integers in increasing order and with length 
      1 <= len(numbers) <= 100.  All integers in numbers are in the
      range(1, 1_000_001).

    Output:

      A single line containing a Python list of all the positive
      integers i in increasing order, where i ** 2 is in numbers.

    Example:

      Input:  [1, 3, 5, 9, 15, 16, 17, 42, 49, 56]

      Output: [1, 3, 4, 7]

    Note: 

      The below code already takes care of reading and printing the lists.
      You only need to implement the function squares.
'''


def squares(numbers):
    pass  # insert code here


# solutions
import math

def squares(numbers):
    return [r for n, r in zip(numbers, map(int, map(math.sqrt, numbers))) if r * r == n]

def squares(numbers):
    out = []
    for n in numbers:
        r = int(math.sqrt(n))
        if r ** 2 == n:
            out.append(r)
    return out

def squares(numbers):
    out = []
    for n in numbers:
        r = math.isqrt(n)
        if r ** 2 == n:
            out.append(r)
    return out

def squares(numbers):
    return [r for n, r in zip(numbers, map(math.isqrt, numbers)) if r * r == n]



numbers = eval(input())

assert numbers == sorted(numbers) and len(numbers) == len(set(numbers))
assert 1 <= len(numbers) <= 100
assert all(1 <= x <= 10 ** 6 for x in numbers)

print(squares(numbers))
