'''
    POSITION TRACKER

    In this problem you should implement a class Tracker, to keep
    track of an (x, y) position. Tracker(x, y) should create a tracker
    object with initial position (x, y), e.g. Tracker(5, 7). If no
    arguments are provided, then Tracker() creates a tracker with
    position (0, 0).

    A tracker should provide the following 5 methods: .print() should
    print the current position of the tracker, and .up(), .down(),
    .left() and .right() should increment y, decrement y, decrement x,
    and increment x of the tracker, respectively. 

    All the 5 methods should return the Tracker object itself, so that
    we can pipeline the operations as follows:

       Tracker(3, 5).right().right().up().print()

    Your task is to implement these five methods and the __init__ method.

    Input:

        A single Python expression instantiating a Tracker, and performing
        a sequence of method calls to the Tracker.

    Output:

        One line for each call to the .print() method, printing the
        current x and y values, separated by space.

    Example:

      Input:  Tracker(5, 7).up().print().up().left().down().print().left().up().print()

      Output: 5 8
              4 8
              3 9

    Note:

      The below code already reads and executes the Python expression
      given as input. Your task is to create the 6 methods in the
      class Tracker.
'''


class Tracker:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def up(self):
        self.y += 1
        return self

    def down(self):
        self.y -= 1
        return self

    def right(self):
        self.x += 1
        return self

    def left(self):
        self.x -= 1
        return self

    def print(self):
        print(self.x, self.y)
        return self

    
eval(input())
