#Exercise 17.3 (Jupyter plotting)

import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 100*(x - 3)**2 + math.e**x

x = np.linspace(0, 10, 1000)
plt.plot(x, [f(xv) for xv in x])
plt.gca().set_yscale('log') #logaritmisk y-akse
plt.show()

#Exercise 17.4 (Jupyter function minimization)
from scipy.optimize import minimize

x_min = minimize(f, [0.0]).x

print(x_min, f(x_min))

plt.gca().set_yscale('log')
plt.plot(x, [f(xv) for xv in x], color="cornflowerblue")
plt.axhline(f(x_min), color="red")
plt.plot([x_min], [f(x_min)], 'gx')
plt.show()

#Exercise 18.1 (numpy)

# a)Generate two 5x5 matrices with entries drawn from a standard normal distribution (mean 0, variance 1).
#numpy.random.normal might come in handy here. Find the inverse of the matrices.
#Check by matrix multiplication, that it is in fact the inverses you have found.

print("\ndelopgave A:")
#loc = mean, scale = sd, size=self explanatory
M = np.random.normal(loc=0.0, scale=np.sqrt(1.0), size=(5, 5))
M_inverse = np.linalg.inv(M)

# Check if M_inverse @ M close to digagonal matrix

print("M_inverse @ M ~= np.eye :", (np.abs(M @ M_inverse - np.eye(5, 5)) < 1e-10).all())

# b) Find the mean of each row and each column of the matrices without using loops. numpy.mean might come in handy here.
print("\ndelopgave B:")
print("Column mean =", M.mean(axis=0))
print("Row mean =", M.mean(axis=1))

# c) Create a 100x100 matrix with entries drawn from the uniform distribution between 0 and 1.
#Find all rows where the sum exceeds 55. Find both the row index and the sum.
#(Try to have a look at the functions numpy.sum and numpy.where).

print("\ndelopgave C:")
M = np.random.random((100, 100))
row_sum = M.sum(axis=1)

#virker som et filter
print("row sums >= 55:", row_sum[row_sum >= 55]) #__getitem__ er lidt vild i np
#der returners indeksene hvor bool er True
print("in rows", np.where(row_sum >= 55)[0].tolist()) #[0] for at få fat i array'et
print(f"{np.where(row_sum >= 55)=}")

#Exercise 18.2 (computing π using sampling)
# a)
def approx_pi(n):
    points = np.random.uniform(size = (2,n))
    print(points.shape)
    res = sum(np.linalg.norm(points, axis=0) <= 1)
    return 4*res/n

#ren prints
for n in [10 ** i for i in range(1,6)]:
    pi_ = approx_pi(n)
    print(f"n: {pi_} err: {abs(np.pi-pi_)}")
print(f"22/7: {22/7} err: {abs(np.pi-22/7)}")

#b)
n = 10000

x = np.random.random(n)
y = np.random.random(n)

print("PI appoximation:", np.average((x**2 + y**2) <= 1) * 4)

import matplotlib.pyplot as plt
import matplotlib.patches as patches

rect = patches.Rectangle((0, 0), width=1, height=1, fill=False)
ax = plt.gca()
ax.add_patch(rect)
ax.set_aspect("equal")

mask = x**2 + y**2 <= 1

plt.plot(x[mask], y[mask], '.r')
plt.plot(x[~mask], y[~mask], '.b')
plt.show()

# Exercise 18.3 (polynomial fit)
import numpy as np
import matplotlib.pyplot as plt

L = [(2, 3), (5, 7), (4, 10), (10, 15), (2.5, 5), (8, 4), (9, 10), (6, 6)]

x, y = zip(*L)

for degree in range(1, 10):
    coefficients = np.polyfit(x, y, degree)

    fx = np.linspace(min(x), max(x), 1000)
    fy = np.polyval(coefficients, fx)

    dist = max(abs(np.polyval(coefficients, x) - y))

    plt.plot(fx, fy, label=f"degree {degree} (distance = {dist:.2f})")
    if dist < 1:
        break

plt.plot(x, y, 'ro')
plt.legend()
plt.show()