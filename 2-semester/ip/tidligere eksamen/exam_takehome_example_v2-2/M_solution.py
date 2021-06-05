'''
    RECTANGLES

    In this exercise we consider "filling" rectangles into a
    rectangular text. We start with H rows, each of length W, only
    containing the character '.'. Rows are indexed top-down 0 to H-1,
    and columns are indexed left-to-right 0 to W-1.

    Then we draw n rectangles into this text. A rectangle has an upper
    left position (r1, c1) and lower right position (r2, c2).  All
    positions spanned by the rectangle are filled with the same
    character (from 'A' to 'Z'). Rectangles are allowed to overlap.    
    Unfilled positions are filled with '.', and all other positions
    are filled with the character for the last rectangle covering the
    position.

    Input:

        The first lines contains three integers H, W and n seperated
        by spaces. Then follows n lines, each describing a rectangle.
        A rectangle is described by a line with five values 
            r1 c1 r2 c2 char
        where r1 and c1 is the upper left corner position (r1 row
        index, c1 column index), r2 and c2 the lower right corner
        position and char is the character to fill the rectangle with.
        Here r1, c1, r2 and c2 are integers and char a single character.

        The input will satisfy:
          1 <= H <= 10
          1 <= W <= 20 
          0 <= n <= 10
          0 <= r1 <= r2 < H
          0 <= c1 <= c2 < W
          'A' <= char <= 'Z'
          
    Output:

        H lines of length W, where each character is either '.'
        or one of the characters from the input specification.

    Example:

      Input:  5 10 4
              2 0 4 6 A
              1 5 3 8 C
              0 7 2 9 B
              3 2 3 2 X

      Output: .......BBB
              .....CCBBB
              AAAAACCBBB
              AAXAACCCC.
              AAAAAAA...
'''


pass  # insert your code here

H, W, n = map(int, input().split())

assert 0 <= H <= 10
assert 0 <= W <= 20

A = [['.'] * W for _ in range(H)]

for _ in range(n):
    values = input().split()
    r1, c1, r2, c2 = map(int, values[:4])
    char = values[4]

    assert 0 <= r1 <= r2 < H
    assert 0 <= c1 <= c2 < W
    assert len(char) == 1 and 'A' <= char <= 'Z'

    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            A[r][c] = char

for row in A:
    print(''.join(row))
