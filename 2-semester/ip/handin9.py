import numpy as np
np.set_printoptions(suppress=True)
from scipy.optimize import linprog

# kilder ----
## https://www.geeksforgeeks.org/python-filter-dictionary-key-based-on-the-values-in-selective-list/
## https://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/


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
source = 'A'
sink = 'F'

edge_from, edge_to, capacity2 = zip(*edges)
edge_from
edge_to
capacity2

string = edge_to + edge_from
unique = []
for char in string[::]:
    if char not in unique:
        unique.append(char)
unique.sort()
uq = unique
uq_dict = {f:i for i, f in enumerate(uq)}
uq_dict # >>> uq_dict {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
source_sink = [source, sink] # ['A', 'F']
delete_items_array = [uq_dict[i] for i in source_sink if i in uq_dict]
delete_items_array # [0, 5]
conservation = np.zeros([len(uq), len(capacity2)])
np.delete(conservation, delete_items_array ,axis = 0)

