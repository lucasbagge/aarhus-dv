import numpy as np
np.set_printoptions(suppress=True)
from scipy.optimize import linprog

#0  1  2  3  4  5  6  7  8
conservation = np.array([
  # 0  1  2  3  4  5  6  7  8
  [ 0,-1, 0, 0, 1, 1, 0, 0, 0],  # B
  [-1, 0, 1, 1, 0, 0, 0, 0, 0],  # C
  [ 0, 0, 0,-1, 0,-1,-1, 0, 1],  # D
  [ 0, 0,-1, 0,-1, 0, 1, 1, 0]   # E
  ]) 


#                 0  1  2  3  4  5  6  7  8
sinks = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1])

#                    0  1  2  3  4  5  6  7  8
capacity = np.array([4, 3, 1, 1, 3, 1, 3, 1, 5])

res = linprog(-sinks,
              A_eq = conservation, 
              b_eq = np.zeros(conservation.shape[0]),
              A_ub = np.eye(capacity.size),
              b_ub = capacity)
print(res)

edges = [('A', 'C', 4),
         ('A', 'B', 3),
         ('C', 'E', 1),
         ('C', 'D', 1),
         ('B', 'E', 3),
         ('B', 'D', 1),
         ('E', 'D', 3),
         ('E', 'F', 1),
         ('D', 'F', 5)]
edge_from, edge_to, capacity2 = zip(*edges)
edge_from
edge_to
capacity2

capacity3 = np.array(capacity2)
capacity3
res2 = linprog(-sinks,
              A_eq = conservation, 
              b_eq = np.zeros(conservation.shape[0]),
              A_ub = np.eye(capacity3.size),
              b_ub = capacity3)

print(res2)

string = edge_to + edge_from
unique = []
for char in string[::]:
    if char not in unique:
        unique.append(char)
unique.sort()
unique = unique[:-1]
unique = unique[1:]
conservation = np.empty([len(unique), len(cap2)])

