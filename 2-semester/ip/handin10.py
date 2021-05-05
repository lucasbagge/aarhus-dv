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
import pylab

"""
  a)

  I den første del af opgaven skal vi definerer en random_walk funktion.
  Den måde jeg har gjort på (ved brug af en yield generator) er at ud fra mine offsets så bevæger
  den sig længere og længere ud. 
  På den måde får jeg et resultat, som minder om det i opgave beskrivelsen.
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
I den anden del skal vi plotte vores frekvens af random walks. 
Jeg var lidt i tvivl om hvordan det korrekte plot igentlig skulle se ud.
Derfor har jeg prøvet mig frem med to metode. En hvor jeg benytter mig af np.histrogram2d, som var en funktion jeg stødte på.
Den anden metode var fra følgende side: https://www.geeksforgeeks.org/random-walk-implementation-python/, hvor jeg egentlig
har lånt koden og forsøgt mig med samme fremgangmåde og synes at jeg får et fint plot med modulet de bruger "pylab".
"""
# Random walk på længden 1000
n = 1000
walk = list(it.islice(random_walk(), 0, n))

xy = list(zip(*walk))

x = list(xy[0])
y = list(xy[1])
# sætter bins til at have en afstand på 1 enhed. 
heatmap, xedges, yedges = np.histogram2d(x, y, bins=[np.arange(min(x),max(x),1),np.arange(min(y),max(y),1)])
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.imshow(heatmap, origin='lower', extent=extent)
plt.imshow(xy, origin='lower', extent=extent)
plt.colorbar()
plt.show()

pylab.title("Random Walk ($n = " + str(n) + "$ steps)")
pylab.plot(x, y)
pylab.show()

# https://stackoverflow.com/questions/61387570/create-infinite-random-walk-using-iterators-in-python
# https://stackoverflow.com/questions/61631246/python-plot-frequency-of-negative-x-y-coordinates
