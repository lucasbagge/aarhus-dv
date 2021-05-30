#Exercise 19.1 (linear program)
from scipy.optimize import linprog
import numpy as np


c = np.array([350, 300])

A_ub = np.array([[ 1,  1],
                            [ 9,  6],
                            [12, 16],
                            [-1,  0],
                            [ 0, -1]])

b_ub = np.array([200, 1566, 2880, -3, -7])

# negates c to make maximization to a minimization problem
result = linprog(-c,
                         A_ub=A_ub,
                         b_ub=b_ub)

print(result)


# Exercise 20.2 (Fibonacci numbers - generator and iterator)

# a
def fib(n):
    fib0 = 0
    fib1 = 1

    for i in range(n):
        yield fib1
        fib0, fib1 = fib1, fib0 + fib1


# b
class FibonacciIteratior:
    def __init__(self, n):
        self.n = n
        self.fib0 = 0
        self.fib1 = 1

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        else:
            if self.n is not None:
                self.n -= 1
            self.fib0, self.fib1 = self.fib1, self.fib1 + self.fib0
            return self.fib0


class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return FibonacciIteratior(self.n)

#Exercise 20.3 (subsets generator)
def subsets_generator(L):
    if len(L) == 0:  # Base Case
        yield []
    else:
        for s in subsets_generator(L[1:]):
            yield s
            yield [L[0]] + s

#Exercise 20.4 (subset sum generator)
def subset_sum(x, L):
    for s in subsets_generator(L):
        if sum(s) == x:
            yield s

#Exercise 20.5 (permutations generator)
def permutations(L):
    if len(L) == 0:
        yield  []
    else:
        for p in permutations(L[1:]):
            for i in range(len(L)):
                yield p[:i] + L[0:1] + p[i:]

def permutations2(L):
    yield from ((s,) + p for i, s in enumerate(L) for p in permutations2(L[:i] + L[i + 1:])) if L else [()]


# Exercise 20.6* (linked list)
class LinkedList:
    class Node:

        # a
        def __init__(self, e):
            self.element = e
            self.next = self

    # a igen
    def __init__(self, values=()):
        self.last = None
        for e in values:
            self.push(e)

    # b
    def empty(self):
        return self.last == None

    # f
    def extend(self, other):
        if other.last != None:
            if self.last == None:  # hvis vores liste ikke har nogen last
                self.last = other.last
            else:  # opdater cyclen
                self.last.next, other.last.next = other.last.next, self.last.next
            other.last = None

    # d
    def pop(self):
        e = self.last.next.element
        if self.last.next == self.last:  # hvis det er den sidste node
            self.last = None
        else:
            self.last.next = self.last.next.next  # opdatere den sidste node's next
        return e

    # c
    def push(self, e):
        node = LinkedList.Node(e)
        if self.last == None:  # hvis det er den første node
            self.last = node
        else:
            node.next = self.last.next  # den nye node's next
            self.last.next = node  # den sidste node's next

    # e
    def __iter__(self):
        if self.last:
            it = self.last.next
            yield it.element
            while it.next != self.last.next:
                it = it.next
                yield it.element

    def __len__(self):
        return sum(1 for e in self)

    def __repr__(self):
        return self.__class__.__name__ + '(' + ', '.join(
            repr(e) for e in self) + ')'