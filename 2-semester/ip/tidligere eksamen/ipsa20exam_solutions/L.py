'''
    RECURSIVE FUNCTION

    Consider the following recursively defined integer function 

        f(n) = f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)

    for n >= 3, and f(n) = 1 for 0 <= n < 3.

    Your task is to write a program that computes f(n).

    Input:

      A single line containing an integer n, where 1 <= n <= 10000.

    Output:

      f(n)

    Example:

      Input:  10

      Output: 2036
'''


n = int(input())

assert 1 <= n <= 10000

'''
# Solution 1
# (on Windows 10: "RecursionError: maximum recursion depth exceeded")
def memoize(f):
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper

@memoize
def f(n):
    return f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3) if n >= 3 else 1

print(f(n))
'''

# Solution 2
F = []
for N in range(n + 1):
    F = F[-2:] + [1 if N < 3 else F[-1] + 2 * F[-2] + 3 * F[-3]]
print(F[-1])
