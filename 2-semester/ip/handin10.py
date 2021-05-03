"""
Exercise 20.7 - handin 10 (random walk)

a)
Create a generator function random_walk that uses yield to generate an infinite 
sequence of points on a 2D integer grid. The first point should be (0,0), and each 
subsequent point a random of the four neighbors of the previous point. E.g. the following sequence:
(0, 0) (1, 0) (1, 1) (2, 1) (2, 0) (1, 0) (0, 0) (0, 1) (-1, 1) (-2, 1) (-1, 1) (-2, 1) (-3, 1) (-2, 1) (-3, 1)...

b)
Use the imshow and colorbar functions from the pyplot module to visualize the 
frequency the different cells are visited in a random walk of length 1000.
Hint. import matplotlib.pyplot as plt; plt.imshow([[1,2,4],[0,3,-1]]); plt.colorbar(); plt.show()
Hint. imshow takes an optional argument extent to adjust the x-axis and y-axis.
Hint. Use itertools.islice to get a finite prefix of an infinite iterator. 
Depending of your approach, collections.Counter might become handy.
"""

"""
  Modules
"""
import random as rd
import itertools as it
import matplotlib.pyplot as plt
import numpy as np

"""
  a)
"""
def random_walk():
  x = y = 0
  offsets = [ (0, 1), (0, -1), (1,0), (-1, 0) ]
  while True:
    yield (x,y)
    dx, dy = rd.choice(offsets)
    x, y = x + dx, y + dy

print(*it.islice(random_walk(), 15))

"""
b)
"""
# Random walk på længden 1000
walk = list(it.islice(random_walk(), 0, 1000))

xy = list(zip(*walk))

x = list(xy[0])
y = list(xy[1])
# sætter bins til at have en afstand på 1 enhed. 
heatmap, xedges, yedges = np.histogram2d(x, y, bins=[np.arange(min(x),max(x),1),np.arange(min(y),max(y),1)])
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.imshow(heatmap, origin='lower', extent=extent)
plt.colorbar()
plt.show()

# https://stackoverflow.com/questions/61387570/create-infinite-random-walk-using-iterators-in-python
# https://stackoverflow.com/questions/61631246/python-plot-frequency-of-negative-x-y-coordinates
