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
#%%
from numpy.core.einsumfunc import _parse_possible_contraction


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
#%%
# a)
@memoize
def lcs_length(x, y):
    def lcs_subsequence(i, j):
        if i and j:
            
            x_end, y_end = x[i - 1], y[j-1]
            if x_end == y_end:
                return lcs_subsequence(i-1, j-1) + 1
            else:
                return max(lcs_subsequence(i, j-1), \
                          lcs_subsequence(i-1, j))
        else:
            return 0
    result = lcs_subsequence(len(x), len(y))

    return result
lcs_length('abracadabra', 'azrael')



#%%
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


# %%
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    #print(n)
    return fib(n-1) + fib(n-2)
%time fib(35)
# %%
def memoize(f):
    cache = {}
    def wrapped(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return wrapped

@memoize
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
%time fib(1)
# %%
A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
A
# %%
def ls(A):
    LIS = [[] for _ in range(len(A))]
    LIS[0].append(A[0])
    
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] < A[i] and len(LIS[j]) > len(LIS[i]):
                LIS[i] = LIS[j].copy()
        LIS[i].append(A[i])
        
    j = 0 
    for i in range(len(A)):
        if len(LIS[j]) < len(LIS[i]):
            j = 1
    return LIS

ls(A)
# %%
len(A)
# %%
def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

print(recMC([1,5,10,25],63))
%time
# %%
