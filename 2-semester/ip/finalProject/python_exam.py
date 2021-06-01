#%%
test = {'B': 3, 'D': 1, 'A': 2, 'F': 7, 'E': 3, 'G': 4}
print(test)
# %%

#%%
from collections import Counter
from itertools import chain

#print(list(test.values())) 

counter = Counter(test.values())
#print(counter)

[key for key, value in test.items() if counter[value] == 1]

#%%

#%%
test = [(3, 1, 2), (-2, 1, 4), (2, 2, 2), (-1, 1, -1)]

sorted(test, key = lambda v: v[0] **2 + v[1]**2+v[2]**2)
# %%
