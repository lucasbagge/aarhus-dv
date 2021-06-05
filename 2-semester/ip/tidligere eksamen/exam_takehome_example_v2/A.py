'''MAZE

   In this problem you should find the shortest distance in a
   rectangular maze from a cell A to a cell B. In each step you can go
   to any of the four neighbouring cells left, right, down and up,
   except cells marked '#'.
   
   Input:

      The first line contains two integers 'rows' and 'columns',
      separated by space.

      The following 'rows' lines contain the maze. Each line contains
      'columns' characters from '.', '#', 'A' and 'B'.

      The maze contains exactly one 'A' and one 'B'.

      2 <= rows * columns <= 10.000

   Output:

      A single line containing the length of the shortest path from A to B.
      Print -1 if no path exists.

   Example (see tests/A/... for more examples):

     Input:   5 6
              .A....
              ###.##
              ......
              ..####
              ....B.

     Output:  11
'''


line = input()
n, m = map(int, line.split())

maze = [input() for _ in range(n)]

def find(symbol):
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == symbol:
                return (i, j)

start = find('A')
finish = find('B')

distance = {start: 0}
Q = [start]
while Q and finish not in distance:
    i, j = Q.pop(0)  # inefficient, but ok

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        i_ = i + di
        j_ = j + dj
        if (0 <= i_ < n and 0 <= j_ < m
            and (i_, j_) not in distance
            and maze[i_][j_] != '#'):
            distance[i_, j_] = distance[i, j] + 1
            Q.append((i_, j_))

print(distance[finish] if finish in distance else -1)
