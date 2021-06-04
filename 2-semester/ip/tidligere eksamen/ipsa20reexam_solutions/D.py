'''
    DIVISIBLE

    Your task is to implement a function divisible(L, x), that given a
    list of positive integers L and a positive integer x, returns a
    list of all integers z, where x * z is in L.

    Input:

      A Python tuple(L, x), where L is sorted list of distinct
      positive integers and x a positive integer, where 
      1 <= len(L) <= 100 and all y in L are 1 <= y <= 1_000_000
      and 1 <= x <= 1_000_000.    

    Output:

      A sorted list of distinct integers z, where x * z is in L.

    Example:

      Input:  ([3, 5, 7, 9, 11, 13, 15, 21, 24, 26], 3)

      Output: [1, 3, 5, 7, 8]

      In the above example 3 * 1 = 3, 3 * 3 = 9, 3 * 5 = 15, 
      3 * 7 = 21 and 3 * 8 = 24 are in the input.

    Note:

      The below code already takes care of the input and output. 
      Your task is only to implement the function divisible.
'''


def divisible(L, x):
    pass  # insert code here


def divisible(L, x):
    return [y // x for y in L if y % x == 0]


L, x = eval(input())

assert isinstance(x, int) and 1 <= x <= 10 ** 6
assert 1 <= len(L) <= 100 and L == sorted(L) and len(L) == len(set(L))
assert all(isinstance(y, int) and 1 <= y <= 10 ** 6 for y in L)

print(divisible(L, x))
