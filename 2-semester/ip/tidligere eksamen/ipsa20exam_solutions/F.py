''' 
    MISSING RECTANGLE CORNER

    A rectangle has four corners (x1, y1), (x1, y2), (x2, y1) and (x2, y2),
    for four integers x1, x2, y1, and y2, where x1 != x2 and y1 != y2.
    Your task is to find the missing corner, given three of the corners.

    Input:  Three lines, each line containing two integers x and y,
            separated by a space, representing a corner point (x, y). 
            It is guaranteed that the three input points are the
            corners of a rectangle as defined above.

    Output: A single line with two integers x and y, separated by a space,
            representing the missing corner point (x, y).

    Example:

      Input:  2 5
              4 3
              4 5

      Output: 2 3
'''


points = {tuple(map(int, input().split())) for _ in range(3)}
xs, ys = map(set, zip(*points))

assert len(points) == 3 and len(xs) == 2 and len(ys) == 2

missing, = {(x, y) for x in xs for y in ys} - points
print(*missing)
