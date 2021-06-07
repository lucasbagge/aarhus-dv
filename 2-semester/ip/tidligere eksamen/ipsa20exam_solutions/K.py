'''REACHABLE POSITIONS

    Consider a rectangular board of n x n squares, each indexed (x, y) 
    with 0 <= x < n and 0 <= y < n, where the lower left corner is (0, 0). 
    We consider a piece that starts at some position start = (x, y) 
    and has a limited number of moves relative to its current position. 
    The moves are described by a list of (dx, dy) pairs, meaning that the 
    piece can move from its current position (x, y) to (x + dx, y + dy).
    E.g. if moves = [(2, 0), (-1, 1), (-1, -1)], then the piece has three
    possible moves (provided the target position is within the limits of the board),
    namely moving two positions to the right, or diagonal left-up or left-down, 
    as illustrated below

        ......
        .x....
        ..S.x.
        .x....
        ......

    Your task is to create a function reachable(n, start, moves) that 
    visualizes all the positions reachable by the piece by one or more moves.

    Input:  

      A single line containing a Python tuple (n, start, moves), where
      n is the dimension of the board, start = (x, y) is the start
      position of the piece, and the moves is a list of (dx, dy)
      pairs, describing valid moves. It is guaranteed that 1 <= n <= 200.

    Output: 

      The output should be n lines with n characters each, where
      each character represents a square on the board. The lower
      left corner is (0, 0). The start position should be marked
      'S', positions reachable by one or more moves 'x', and
      unreachable positions '.'.

    Example:

      Input:  (6, (0, 0), [(2, 0), (-1, 1), (-1, -1)])

      Output: .x.x.x
              x.x.x.
              .x.x.x
              x.x.x.
              .x.x.x
              S.x.x.

    Note:

      Note the below code already contains code for reading the
      input. You should only implement the body of the function
      reachable.

'''


def reachable(n, start, moves):
    Q = {start}
    seen = {start}
    while Q:
        (x, y) = cell = Q.pop()
        for dx, dy in moves:
            cell_ = (x_, y_) = (x + dx, y + dy)
            if 0 <= x_ < n and 0 <= y_ < n and cell_ not in seen:
                seen.add(cell_)
                Q.add(cell_)

    for y in range(n)[::-1]:
        for x in range(n):
            char = '.'
            if (x, y) in seen: char = 'x'
            if (x, y) == start: char = 'S'
            print(char, end='')
        print()


n, start, moves = eval(input())

assert 1 <= n <= 200

reachable(n, start, moves)
