"""
HANDIN 5 (eight queens puzzle)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:

    <
    I denne opgave har jeg lavet to funktioner; possible og solve.
    Possible checker for hver række og kolonne om der er en løsning.
    solve løser problemet ved at kigge i hver række, kolonne og diagonal om
    der er en dronning i forvejen.
    Med en opfordring fra sidste aflevering har jeg tilføjet noter undervejs 
    i koden, så det gør det letter at se hvad der sker undervejs. 
    En ulempe er at løsningen er langsom.
    >
"""

import numpy as np

N = int(input("Antal dronninger der skal løses: \n"))
chessboard = np.zeros([N,N],dtype=int)
chessboard = chessboard.tolist()

def possible(chessboard, row, col): # Først funktion til at se om problemet kan løses.
    l=len(chessboard) # Tager hele længden af skakbrættet
    for i in range(l): # Ser om der er nogle dronningenri rækken.
        if chessboard[row][i]==1: # Hvis den findes så skal vi retuner falsk.
            return False
    for i in range(l):  # Ser om der er nogle dronninger i kolonnen.
        if chessboard[i][col]==1: # Hvis der er en dronning retuner falsk.
            return False
    # Hvis ikke ovenstående er tilfældet, så går den videre.
    for i in range(l): # Går gennem alle rækker.
        for j in range(l): # Går gennem alle kolonner.
            if chessboard[i][j]==1: # Ser om der er en dronning.
                if abs(i - row) == abs(j - col): # Ser om der er en dronning i diagonalen
                    return False 
    return True 

def solve(chessboard):
    l=len(chessboard) # Længden som i forrig funktion.
    for row in range(l): # Føtst for hver række.
        for col in range(l): # Først for hver kolonne.
            if chessboard[row][col] == 0: # Hvis der ingen dronning er kan vi indsætte 1.
                if possible(chessboard, row, col): # Check om cellen er tom.
                    chessboard[row][col] = 1 # Hvis den er tom kan vi indsætte 1.
                    solve(chessboard) # Her kommer den rekursive løsning ind i billede.
                    if sum(sum(a) for a in chessboard) == l: # Check om vi har nået alle mulige løsninger.
                        return chessboard 
                    chessboard[row][col] = 0 # Fjerner de tidliger dronninger
    return chessboard #means we searched the space, we can return our result


print(np.matrix(solve(chessboard)))
...

