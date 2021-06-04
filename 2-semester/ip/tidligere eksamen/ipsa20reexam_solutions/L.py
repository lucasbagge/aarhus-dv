'''
    COIN COLLECTOR

    Consider a rectangular maze of height x width cells. Each cell is
    either blocked by a wall '#', a free cell '.', a cell with a gold
    coin 'x', or a starting cell 'S'. A maze contains exactly one 'S'.
    Your task is to compute how many gold coins can be collected
    starting from 'S' when you are only allowed to move horizontally or
    vertically to adjacent cells not blocked by a wall. See example below.

    Input:

      The first line contains two positive integers height and width,
      separated by space, where 1 <= height <= 25 and 1 <= width <= 25.
      The following height lines each contain a row of the maze.  Each
      row has length width and contains only characters from '#Sx.'.

    Ouput: 

      A single line with the number of gold coins collectable from 'S'.

    Example:

      Input:  7 9
              #########
              #..x.x.x#
              ###.#####
              #.#S.x#x#
              #.#####.#
              #.#x.x.x#
              #########

      Output: 4
'''


pass  # insert code here


# solution
height, width = map(int, input().split())
maze = [input() for _ in range(height)]

assert 1 <= width <= 25
assert 1 <= height <=25
assert all(len(row) == width for row in maze)
assert all(char in '#Sx.' for row in maze for char in row)

start, = [(i, j)
          for i, row in enumerate(maze)
          for j, char in enumerate(row)
          if char == 'S']

coins = 0
seen = {start}
visit = {start}
while visit:
    r, c = visit.pop()
    if maze[r][c] == 'x':
        coins += 1
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cell = (r_, c_) = (r + dr, c + dc)
        if (0 <= r_ < height and 0 <= c_ < width
            and maze[r_][c_] != '#' and cell not in seen):
            
            seen.add(cell)
            visit.add(cell)

print(coins)
