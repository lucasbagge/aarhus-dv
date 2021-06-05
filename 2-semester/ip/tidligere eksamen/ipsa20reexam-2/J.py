'''
    ITERABLE Z-COUNT

    In this task you should create an iterable class Count.  

    An object of class Count is created using Count(n), where n a
    positive integer. When iterating over a Count(n) object, it should
    generate an infinte sequence of pairs:

      (1, 1) (1, 2) ... (1, n) (2, 1) (2, 2) ... (2, n) (3, 1) ...

    Example usages of class Count: 

      Example of using a Count object as an iterable in a for-loop:

        for x in Count(2):
            print(x)

      should print

        (1, 1)
        (1, 2)
        (2, 1)
        (2, 2)
        (3, 1)
        (3, 2)
        (4, 1)
        ...

      Example using iter and next:

        count = Count(3)
        it = iter(count)
        for _ in range(10):
            print(next(it), end=' ')

      should print

        (1, 1) (1, 2) (1, 3) (2, 1) (2, 2) (2, 3) (3, 1) (3, 2) (3, 3) (4, 1)     

    Input:  

      A single line containing a Python expression using the class Count.

    Output:

      The result of evaluation the expression.

    Example:

      Input:  [x for x, _ in zip(Count(3), range(7))]

      Output: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1)]

    Note:

      The below code already handles the input and output. 
      Your task is only to implement the class Count.
'''


class Count:

    """Iterator that counts upward forever."""

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        x = 1
        while True:
            for y in range(1, self.n + 1):
                yield(x, y)
            x += 1


expression = input()
print(eval(expression))
