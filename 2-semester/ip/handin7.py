"""
HANDIN 7 (Convex hull)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:

    <
	I denne uge har vi skulle implementer en algoritme til kaldet Convex hull.
	Jeg er kommet frem til en løsning til opgave a, c og d. I opgave c har jeg taget brug af at beregne øvre og nedre
	dele og herefter samle dem.
	I opgave d skulle vi implemterer nogle test af vores funktion i form af assert og doctest. Jeg har delt min funktion fra c
	op i to dele, hvor i den ene benytter jeg nogle simple assert statement for at se om min funktion virke. For at benytte doctest
	har jeg givet et eksempel på hvordan jeg regne mit funktion conv_hull vil være. 
	Jeg har nogle mangle, som jeg gerne vil have feedback på:
	* i opgave b) kunne jeg ikke finde ud af at bruge hintene til at lave en plot_hull funktion. Jeg har svært ved at se hvordan det skal
	gøres?
	* Jeg kunne måske i d gøre mere ud af at lave flere test af min funktion?
	* Jeg bruger at array til at plotte funktionen, er det ok eller en dum løsning?
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

# b) ----

#def plot_hull(points, polygon):
#    polygon = np.array(polygon)
#
#	fig = plt.figure
#	plt.plot(points[:,0],points[:,1], 'r-')
#	plt.plot([points[-1,0],points[0,0]],[points[-1,1],points[0,1]], 'b-')
#	plt.plot(polygon[:,0],polygon[:,1],"go")
#	return fig

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
	return np.array(L)

P = random_points(10)
L = convex_hull(P)
print("convex hull: \n", L)
P = np.array(P)
plt.gca()
plt.plot(L[:,0],L[:,1], 'r-')
plt.plot([L[-1,0],L[0,0]],[L[-1,1],L[0,1]], 'b-')
plt.plot(P[:,0],P[:,1],"go")

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
  array([[0.5, 2. ],
       [1. , 1. ],
       [2. , 3. ]])
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