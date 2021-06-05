'''SUM

   Compute the sum of n integers x_1, ..., x_n.

   Input:

     The first line contains an integer n, 1 <= n <= 100, and the
     following n lines contain x_1, ..., x_n, one integer per line,
     where -100 <= x_i <= 100.

   Output:

     Print a single line with the integer sum x_1 + x_2 + ... x_n.

   Example (see tests/D/... for more examples):

     Input:   5
              2
              3
              1
              -7
              4

     Output:  3
'''


print(sum(int(input()) for _ in range(int(input()))))
