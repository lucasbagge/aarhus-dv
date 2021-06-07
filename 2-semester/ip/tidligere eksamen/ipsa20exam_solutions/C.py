'''
    FUNCTION TABLE

    Your task is to implement a function print_table(f, n, m), that
    as arguments takes a function f and two non-negative integers n
    and m, where 0 <= n <= 25 and 0 <= m <= 25. The function f is
    assumed to take two integers as arguments and to return an integer.
    Your task it to print f(i, j) for all i and j, where 0 <= i <= n
    and 0 <= j <= m.

    Input:

        The first line contains a Python lambda expression taking two
        integer arguments i, j and returning an integer value. 
        We let f denote this function.
        The second line contains two integers n and m, separated by space,
        and where 0 <= n <= 25 and 0 <= m <= 25.

    Output:

        n + 1 lines, each containing m + 1 integers separated by
        space. The j'th value in row i is f(i, j):

            f(0,0) f(0,1) f(0,2) ... f(0,m)
            f(1,0) f(1,1) f(1,2) ... f(1,m)
               .      .      .          .
               .      .      .          .
            f(n,0) f(n,1) f(n,2) ... f(n,m)

    Example:

      Input:  lambda i, j: 2 * i + j
              4 6

      Output: 0 1 2 3 4 5 6 
              2 3 4 5 6 7 8 
              4 5 6 7 8 9 10 
              6 7 8 9 10 11 12 
              8 9 10 11 12 13 14

    Note:

      The below code already takes care of reading the two input lines
      and calling print_table. You only need to implement the body
      of the function print_table.
'''


def print_table(f, n, m):
    for i in range(n + 1):
        print(*[f(i, j) for j in range(m + 1)])
        

f = eval(input())
n, m = map(int, input().split())

assert 0 <= n <= 25 and 0 <= m <= 25

print_table(f, n, m)
