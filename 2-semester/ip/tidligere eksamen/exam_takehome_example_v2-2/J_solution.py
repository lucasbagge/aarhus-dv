'''
    NON-DIVISIBLE

    In this problem you should write a function not_divisible(n, L),
    that given a positive integer n and a non-empty list L of distinct
    positive integers, should return a sorted list of all integers in
    range(n) that are not divisible by an element in L.

    In the test inputs 0 < n <= 1000, len(L) <= 100, and 0 < L[i] < n.

    Example:

        not_divisible(50, [2, 3, 5])
        
          = [1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49] 

    Note: The below code reads a pair (n, L) from input and prints the result
    of calling not_divisible(n, L). Your task is only to write the code for
    not_divisible.
'''


def not_divisible(n, L):
    pass  # write your code here

#  --Solution below this line--
def not_divisible(n, L):
    return sorted(set(range(n)) - {x for f in L for x in range(0, n, f)})


n, L = eval(input())  # read (n, L) from input 
print(not_divisible(n , L))
