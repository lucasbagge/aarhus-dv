'''FIBONACCI

   Compute the n'th Fibonacci number fib(n), defined recursively:

     fib(0) == 0, fib(1) == 1, fib(n) = fib(n - 1) + fib(n - 2)

   Input:

      A single line containing an integer n, 0 <= n <= 10.000

   Output:

      A single line with the integer fib(n).

   Example (see tests/C/... for more examples):

     Input:   10

     Output:  55
'''


def fib(n):
    '''Recursive solution'''
    return n if n < 2 else fib(n - 1) + fib(n - 2)


def memoize(f):
    '''memoize function decorator'''
    
    answers = {}

    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]

    return wrapper


def fib_iterative(n):
    '''Non-recursive solution'''

    answers = [0, 1]
    while len(answers) <= n:
        answers.append(answers[-1] + answers[-2])
    return answers[n]


@memoize
def fib_memoized(n):
    '''Recursive solution using memoization'''

    return n if n < 2 else fib_memoized(n - 1) + fib_memoized(n - 2)


n = int(input()) # Read integer n from standard input

print(fib(n))
#print(fib_memoized(n))
#print(fib_iterative(n))
