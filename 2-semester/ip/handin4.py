"""
HANDIN 4 (triplet distance - part II)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:
    <
    I denne uges aflevering har vi skulle træne funktioner og rekursion.
    Det har været udforende, men en sjov og lærerig process.
    Den første opgave var min tanke at det input man skulle give blev til en
    random træ, så der har jeg gjort brug af **randiant.
    I opgave b voldte en hel del problemer, men i sin essens skulle man
    gøre brug af funktioner fra forrig aflevering og bruge dem til at laver
    vores leaves og triplet.
    Opgave c fik vi egentlig givet funktionen som vi skulle bruge til at måle
    afstanden, men mit problem var at helt forstå tanken om at måle afstanden.
    I den sidste opgave skulle vi generer en masse træer og måle tiden. Der
    har jeg brugt meget af den metode Gerth bruger i sin forlæsning om lists.
    >
"""

from random import randint
from time import time
from matplotlib import pyplot as plt

# a)
def generate_tree(L):
    # base case
    if len(L) == 1: 
        return L[0]
    split = randint(1, len(L)-1)
    left = L[:split]
    right = L[split:]
    # recursion
    return (generate_tree(left), generate_tree(right))

L = ['A', 'B', 'C', 'D', 'E', 'F']
print("a) Træer: " ,generate_tree(L))

# b)

# canonical_triplets er fra sidste afleverin
def canonical_triplets(A, B):
  can = [(x, (y,z)) for x in A for y in B for z in B if y < z]
  return can

# anchored_triplets er fra sidste afleverin
def anchored_triplets(A,B):
  left = canonical_triplets(A,B)
  right = left
  right += canonical_triplets(B,A)
  return list(( right))

def generate_triplets(T):
  if isinstance(T, str):
    return [T], []
  else:
    left = T[0]
    right = T[1]
    
    left_labels, left_triplets = generate_triplets(left)
    right_labels, right_triplets = generate_triplets(right)
    
    labels = left_labels + right_labels
    triplets = left_triplets + right_triplets
    
    anchored_triplet = anchored_triplets(left_labels, right_labels)
  return labels, triplets + anchored_triplet

print("b) output: " ,generate_triplets(((('A','F'),'B'),('D',('C','E')))) )

# c) 
def triplet_distance(T1, T2):
  gen_T1 = generate_triplets(T1)
  gen_T2 = generate_triplets(T2)
  
  n = len(gen_T1[0])
  x = gen_T1[1]
  y = gen_T2[1]
  
  intersec = len(set(x) & set(y))
  
  return (n * (n - 1) * (n - 2)) // 6 - intersec

print("c) distance between trees: ",triplet_distance(((('A','F'),'B'),('D',('C','E'))), (((('D','A'),'B'),'F'),('C','E'))) )

# d) 
ns = range(10_0, 1_000_0, 10_0)
time_string = []
time_list = []
s = []

for n in ns:
  start = time()
  for _ in range(n):
    s += generate_tree("abc")
  end = time()
  time_list.append(end-start)
print("number of tree created: ", len(s))
plt.plot(ns, time_list)
plt.show()
...
