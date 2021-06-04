'''
    PLOT FUNCTION

    Given a function f mapping integers to integers, and four integers
    x1, x2, y1 and y2, representing intervals [x1, x2] and [y1, y2],
    your task is to make a simple ASCII plot of f in the range 
    [x1, x2] x [y1, y2]. See example below for the function 

        f(x) = (x - 3) ** 2 // 10 - 4.  

    The lower left corner is (x1, y1) and the upper right corner is
    (x2, y2). Each position (x, y) should contain one of the five
    characters 'X', '+', '-', '|' and '.'. If f(x) == y, then the
    position should be marked 'X'. The x-axis and y-axis should be
    marked by '-' and '|', i.e. positions with y == 0 and x == 0
    respectively, and their intersection '+', i.e. the position (0,
    0). A 'X' has preference over an axis. All other positions should
    contain '.'.


    Input: 

      Two lines. The first line is a Python lambda expression
      representing the function f, and the second line contains the
      four integers x1, x2, y1 and y2, separated by integers,
      satisfying

      -100 <= x1 < 0 < x2 <= 100 and -100 <= y1 < 0 < y2 <= 100

    Output:

      An ASCII plot as described above, containing y2 - y1 + 1 lines,
      each containing x2 - x1 + 1 characters from 'X+-|.'.

    Example:

      Input:  lambda x: (x - 3) ** 2 // 10 - 4
              -10 20 -5 10

      Output: .X........|..............X.....
              ..........|....................
              ..X.......|.............X......
              ..........|....................
              ...X......|............X.......
              ..........|....................
              ....X.....|...........X........
              ..........|....................
              .....X....|..........X.........
              ..........|....................
              ------X---+---------X----------
              .......X..|........X...........
              ........X.|.......X............
              .........X|......X.............
              ..........XXXXXXX..............
              ..........|....................

    Note:

      The below code already takes care of reading the input. 
      Your task is only to write the function plot_function.
'''


def plot_function(f, x1, x2, y1, y2):
    pass  # insert code here


f = eval(input())
x1, x2, y1, y2 = map(int, input().split())
plot_function(f, x1, x2, y1, y2)
