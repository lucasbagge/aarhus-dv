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
