"""
HANDIN 8 ()
This handin is done by (study ids and names of up to three students):
    202004972 <Lucas Bagge>
Reflection upon solution:
    <
    Først definer jeg min decorator memoize, som er helt mangen til hvad vi så i forlæsning om dynamic programming slide 6.
    Der er egentlig to dele af løsningen til denne opgave. En del a) som beder om at give længden af den optimale streng og
    i b skal vi give den længste streng. Jeg har valgt at slå de to dele sammen. For mig giver det bedre mening at have en 
    enkelt funktion som spytter det output ud. 
    Til selve min LCS funktion, så deler jeg den op i to funktioner LCS og lcs_subsequence. 
    lcs_subsequence kigger strengene igennem fra enden og hvis x og y har nogen ligheder så vil
    de falde ind i den indre funktion. Hvis vi når max så kigger den på længden af stengene
    og den returner den længste. Her har jeg fået inspiration af Knapsack alogritmen.
    >
"""

# til opgaven http://wordaligned.org/articles/longest-common-subsequence

def memoize(f):
    '''
    Implementer nøjagtig samme memoize decorator fra
    dynamic_programming slide 6
    '''
    answers= {}
    def wrapper(*args):
        #key = tuple(args) 
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper

# a)
@memoize
def lcs_length(x, y):
    def lcs_subsequence(i, j):
        if i and j:
            x_end, y_end = x[i - 1], y[j-1]
            if x_end == y_end:
                return lcs_subsequence(i-1, j-1) + 1
            else:
                return max(lcs_subsequence(i, j-1), lcs_subsequence(i-1, j))
        else:
            return 0
    result = lcs_subsequence(len(x), len(y))

    return result
lcs_length('abracadabra', 'azrael')


# b)
@memoize
def LCS(x, y):
    def lcs_subsequence(i, j):
        if i and j:
            x_end, y_end = x[i-1], y[j-1]
            if x_end == y_end:
                return lcs_subsequence(i-1, j-1) + [x_end]
            else:
                return max(lcs_subsequence(i, j-1), lcs_subsequence(i-1, j), key=len)
        else:
            return []
    result = lcs_subsequence(len(x), len(y))

    return ''.join(result)

LCS('abracadabra', 'azrael')
('abca', 'acba')


def lcs(x,y):
    m=len(x)
    n=len(y)

    #Syntax is column*rows for memoization table for m*n matrix
    L=[[None]*(n+1) for i in range(m+1)]
    
    #Loop over the memoization table
    for i in range(m+1):
        for j in range(n+1):
            #Initializing first row and cloumn of memoization table
            if i == 0 or j == 0:
                L[i][j]=0
            #Diagonal condtion if equal
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            #Diagonal if value is not equal
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    
    #The final resullt
    return L[m][n]

x=input("First string : ")
y=input("Second string: ")
print("The length of LCS is : ",lcs(x,y))
