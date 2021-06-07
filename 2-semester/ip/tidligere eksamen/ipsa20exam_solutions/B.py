'''
    COUNT

    Print the numbers 1 2 ... n. 

    Input:

        A single line with an integer n, where 1 <= n <= 1000

    Output:

        A single line with the integers 1, 2, 3, ..., n,
        in increasing order separated by space.

    Example:

      Input:  7

      Output: 1 2 3 4 5 6 7
'''


n = int(input())

assert 1 <= n <= 1000

print(*range(1, 1 + n))
