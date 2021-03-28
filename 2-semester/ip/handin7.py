"""
HANDIN 7 (Convex hull)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:

    <
    Jeg har kigget på rettelser og fjeret i min convex_hull at den giver mig en array
    I b har jeg tilføjet en plt_hull funktion. Den giver mig et plot som jeg er okay tilfreds med,
    men den er ikke fuldstændig en til en med Gerths plot.  
    >
"""
# Moduler ----
import random as ra
import matplotlib.pyplot as plt
import numpy as np

# a) ----
def random_points(n):
  x_coordinate = []
  y_coordinate = []
  not_one = 1
  for i in range(0,n):
    x = ra.random()
    y = ra.random()
    x_coordinate.append(x)
    y_coordinate.append(y)
  x_coordinate = [0.99 if x == 1 else x for x in x_coordinate]
  y_coordinate = [0.99 if x == 1 else x for x in y_coordinate]
  return [(x,y) for x,y in zip(x_coordinate, y_coordinate)]
print("Mine random tal par: \n", random_points(5))

# lternativ og mere fimpel

def random_points2(n):
    return [(ra.random(),ra.random()) for i in range(n)]
print("Mine random tal par: \n", random_points2(5))

# b) ----
def plot_hull(points, polygon):
  link_hole_plot = list(points[i] for i in [0,-1])
  x0,y0  = list(zip(*link_hole_plot))
  x1,y1  = list(zip(*points))
  x2,y2  = list(zip(*polygon))
  plt.plot(x0, y0, "r-")
  plt.plot(x1, y1, "r-")
  plt.plot(x2, y2, "go")
  plt.show()
  
# c) ----
# Jeg kunne ikke få left_turn til at virke, men gjorde jeg det med right turn ville det virke.
def right_turn(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return False
	return True
	
# Algoritmen til convex hull:
def convex_hull(P):
	P.sort() # Sorter punkter
	L_upper = [P[0], P[1]] # Starter med den øvre del
	# Beregning hvor jeg cecker om vi skal sletter noget af den øvre del. 
	for i in range(2,len(P)):
		L_upper.append(P[i])
		while len(L_upper) > 2 and not right_turn(L_upper[-1],L_upper[-2],L_upper[-3]):
			del L_upper[-2]
	L_lower = [P[-1], P[-2]] # Den nedre del.
	# Samme beregning som den øvre del.
	for i in range(len(P)-3,-1,-1):
		L_lower.append(P[i])
		while len(L_lower) > 2 and not right_turn(L_lower[-1],L_lower[-2],L_lower[-3]):
			del L_lower[-2]
	del L_lower[0]
	del L_lower[-1]
	L = L_upper + L_lower # Bygger hele stykket.
	return list(L)

# plot
points = random_points(1000)
test = convex_hull(points)
plt.clf()
plot_hull(test, points)

# d) ----
## assert
def convex_hull(P):
    P.sort()
	L_upper = [P[0], P[1]]
	assert (len(L_upper) == 2)
	for i in range(2,len(P)):
		L_upper.append(P[i])
		while len(L_upper) > 2 and not right_turn(L_upper[-1],L_upper[-2],L_upper[-3]):
			del L_upper[-2] 
	L_lower = [P[-1], P[-2]]
	#assert (len(L_lower) == 2)
	for i in range(len(P)-3,-1,-1):
		L_lower.append(P[i])
		while len(L_lower) > 2 and not right_turnL_lower[-1],L_lower[-2],L_lower[-3]):
			del L_lower[-2]
	del L_lower[0]
	del L_lower[-1]
	L = L_upper + L_lower
	assert (isinstance(L, list))
	return np.array(L)

L = convex_hull(random_points(10))
assert L.shape == (len(L), 2)
assert (L.ndim == 2)

## Doctest
  def convex_hull(P):
      '''
  >>> convex_hull([(0.5,2),(1,1), (2,3)])
  [(0.5, 2), (1, 1), (2, 3)]

  '''
	P.sort() # Sort the set of points
	L_upper = [P[0], P[1]] # Initialize upper part
	# Compute the upper part of the hull
	for i in range(2,len(P)):
		L_upper.append(P[i])
		while len(L_upper) > 2 and not right_turn(L_upper[-1],L_upper[-2],L_upper[-3]):
			del L_upper[-2]
	L_lower = [P[-1], P[-2]]	# Initialize the lower part
	# Compute the lower part of the hull
	for i in range(len(P)-3,-1,-1):
		L_lower.append(P[i])
		while len(L_lower) > 2 and not right_turn(L_lower[-1],L_lower[-2],L_lower[-3]):
			del L_lower[-2]
	del L_lower[0]
	del L_lower[-1]
	L = L_upper + L_lower		# Build the full hull
	return np.array(L)

import doctest
doctest.testmod(verbose=True)
