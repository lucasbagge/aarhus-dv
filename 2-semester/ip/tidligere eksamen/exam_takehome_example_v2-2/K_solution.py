'''
    WINNER

    A group of people are playing n games. For each of the n games
    exactly one of the players earns between 1 and 10 points. The
    overall winner is the player having earned the most points. Your
    task is to print the overall winner (or if it is a draw), given the
    winners of the n games and the points earned.
             
    Input:

        The first line contains a positive integer n. Then follows n
        lines, one line for each game, containing the name of the player
        getting points for the game and the points earned, separated by
        space.

        In the test inputs 1 <= n <= 100, each name is a string of 1-20
        characters from a-z and A-Z, and 1 <= points for game <= 10.

    Output:

        The name of the player achieving the maximum number of points.
        Print 'DRAW' if two or more players achieve the same maximum
        number of points.
        
    Example:

      Input:  6
              Lars 5
              Peter 3
              Gerth 7
              Peter 2
              Lars 2
              Peter 3

      Output: Peter

      In the above example Lars and Gerth score a total of 7 points, and
      Peter scores 8 points.
'''


pass  # write your code here


scores = {}

n = int(input())

for _  in range(n):
    player, score = input().split()
    score = int(score)
    scores[player] = scores.get(player, 0) + score

rank = sorted(scores, key=lambda player: scores[player], reverse=True)

if len(rank) == 1 or scores[rank[0]] > scores[rank[1]]:
    print(rank[0])
else:
    print('DRAW')
