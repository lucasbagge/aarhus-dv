'''
    INTERVAL SUM

    Input:

      A single line with two integers a and b, separated by space,
      where 1 <= a <= b <= 1_000_000.

    Ouput:

      A single line with the sum a + (a + 1) + ... + (b - 1) + b.

    Example:

      Input:  5 10

      Output: 45
'''


pass  # insert code here

a, b = input().split()
a = int(a)
b = int(b)

assert 1 <= a <= b <= 1_000_000

print(sum(x for x in range(a, b + 1)))
