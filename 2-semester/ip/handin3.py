"""
HANDIN 3 (triplet distance - part I)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:
    <
    I denne aflevering har jeg kommet rundt omkring de forskellige tuples og
    list comprehension vi har fået undervisning i.
    I a) definerer jeg en string der generarer flere labels, hvor jeg brug `chr` til at give mig en string.
    Den del af denne aflevering jeg er mest i tvivl om er b), hvor jeg har bruge en for løkke til at bytte rundt,
    om tuplen. Der går noget galt da jeg skal kører den 3 gange får mit output er korrekt, så den kan forbedres.
    I ophave c) bruger jeg hintet givet i opgave beskrive og skriver `x < y`, som sørger vi får det korrekte output.
    De sidste to opgaver d og e bruger jeg næsten den samme metode, hvor jeg i d egentlig er mere restiktiv med min
    definition, hvor jeg tilføjer y < z, mens i e undlader jeg den restriktion.
    Nogle ting der kan forbedres er i opgave b, som jeg er i tvivl om vil blive godkent og så tænker jeg at
    man kan kombinerer nogle af mine funktioner i hinanden.

    >
"""

from random import randint

# a)
def generate_labels(n):
  letters = [chr(x) for x in range(ord('A'), ord('A') + n)]
  return letters

print("a) output af generate_labels : ", generate_labels(8))

# b)
def permute(n):
  for i in reversed(range(1, len(n))): 
    j = randint(0, i)  
    n[i], n[j] = n[j], n[i]
  return n

print("b) output af permute: ",permute(generate_labels(5)))

# c)
def pairs(n):
  par = [(x,y) for x in n for y in n if x < y]
  return par 

print("c) output af pairs: ", pairs(['A', 'F', 'B']))

# d)
def canonical_triplets(A, B):
  can = [(x, (y,z)) for x in A for y in B for z in B if y < z]
  return can

print("d) output af canonical_triplets: ", canonical_triplets(['A', 'B'], ['C', 'D', 'E']))

# e)
def anchored_triplets(A,B):
  left = canonical_triplets(A,B)
  right = canonical_triplets(B,A)
  return (left, right)
print("e) ourput af anchored_triplets",anchored_triplets(['A', 'F', 'B'], ['D', 'C', 'E']))
...
