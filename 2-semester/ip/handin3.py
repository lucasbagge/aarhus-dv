"""
HANDIN 3 (triplet distance - part I)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:
    <
    Rettede koden til at fik lavede det til en liste i min anchored_triplet funktion.
    >
"""
#%%
from random import randint
#%%
# a)
def generate_labels(n):
  letters = [chr(x) for x in range(ord('A'), ord('A') + n)]
  return letters

print("a) output af generate_labels : ", generate_labels(8))
#%%
# b)
def permute(n):
  for i in reversed(range(1, len(n))): 
    j = randint(0, i)  
    n[i], n[j] = n[j], n[i]
  return n

print("b) output af permute: ",permute(generate_labels(5)))
#%%
# c)
def pairs(n):
  par = [(x,y) for x in n for y in n if x < y]
  return par 

print("c) output af pairs: ", pairs(['A', 'F', 'B']))
#%%
# d)
def canonical_triplets(A, B):
  can = [(x, (y,z)) for x in A for y in B for z in B if y < z]
  return can

print("d) output af canonical_triplets: ", canonical_triplets(['A', 'B'], ['C', 'D', 'E']))
#%%
# e)
def anchored_triplets(A,B):
  left = canonical_triplets(A,B)
  right = left
  right += canonical_triplets(B,A)
  return list(( right))
print("e) ourput af anchored_triplets", anchored_triplets(['A', 'F', 'B'], ['D', 'C', 'E']) )
...

# %%
