'''
    WALK

    In this problem you should read a "walk" from input, consisting of a
    start position (x, y), a sequence of moves 'E', 'W', 'N' and 'S',
    and a final line containing 'STOP'. An 'E' increments x by one, 'W'
    decrements x by one, 'N' increments y by one, and 'S' decrements y
    by one. Your output should be the final position of the walk.

    Input:

        The first line contains two integers x and y separated by a
        space. (x, y) is the start position of the walk. The following
        zero or more lines each contain one of the characters 'E', 'W',
        'N' or 'S', each describing one move. The final line contains
        the string 'STOP'.

        The start position (x, y) satisfies -100 <= x, y <= 100 and the
        input contains at most 100 moves.

    Ouput:

        Two integers x and y, separated by space, where (x, y) is the
        final position reached by the walk.

    Example:

      Input:  3 5
              N
              N
              W
              S
              E
              STOP

      Output: 3 6

      The above example describes the following walk:

        (3, 5) -N-> (3, 6) -N-> (3, 7) -W-> (2, 7) -S-> (2, 6) -E-> (3, 6)
'''


x, y = map(int, input().split())

assert -100 <= x <= 100 and -100 <= y <= 100

while True:
    line = input()
    if line == 'STOP':
        break

    assert len(line) == 1 and line in 'NSEW'
    
    if line == 'E': x += 1
    if line == 'W': x -= 1
    if line == 'N': y += 1
    if line == 'S': y -= 1

print(x, y)
