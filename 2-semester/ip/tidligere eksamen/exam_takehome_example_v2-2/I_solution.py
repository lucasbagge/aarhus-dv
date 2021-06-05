'''
    INCREASE

    Your taks is to read n integers, x1, x2, ..., xn, and
    to identify the xi, where xi > xj for all 1 <= j < i.

    Input:

        The first line contains an integer 1 <= n <= 1000,
        that is the number of xi to read.
        Then follows n lines contain the n integers x1,...,xn, 
        one integer xi per line.

    Output:

        n lines, each line containing either the value 0 or 1.
        The i'th output should be 1 if and only if xi is larger
        than all xj's seen so far.
        Note that the first output line always contains 1.

    Example:

      Input:  7
              5
              3
              7
              10
              8
              2
              11            

      Output: 1
              0
              1
              1
              0
              0
              1             
'''


pass  # write your code here

n = int(input())
max_so_far = None
for _ in range(n):
    value = int(input())
    if max_so_far == None or max_so_far < value:
        max_so_far = value
        print(1)
    else:
        print(0)

