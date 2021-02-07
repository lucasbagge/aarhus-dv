import numpy as np
import matplotlib.pyplot as plt

# Opgave 2.2 beregn længde og vinkler i radianer, som multiplum af pi

a1 = 0.0
a2 = 1.0

b1 = 1.0
b2 = -1.0

c1 = -0.5
c2 = −0.8660254037844386

# længden af a og vinklerne i både radianer, som multiplum af pi og i grader

np.sqrt(a1**2 + a2**2)
a = np.array([0.0,1.0])
np.linalg.norm(a)

# Når vi beregner vinklen så skal vi bytte rundt om x og y.
# v = [x,y] i `np.arctan2(y,x)`

# vinklen i radianer
np.arctan2(a2, a1)
# vinklen i grader
np.arctan2(a2, a1) / np.pi

# kopir bare til det næste tre opgaver

# Opgave 2.3
## 

x = np.linspace(1.0, 7.0, 100)
y = (2*np.sin(x))/(1 + x**2)
fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()

help(print)

x = 1
while x <= 5:
print(x, end=' ')
x = x + 1
print('and', x)

#% laver devision
x = 1
while x <= 5:
  print(x, end = " ")
  x = x + 1
print("and", x)

from random import randint
while True:
  x = randint(1,10)
  y = randint(1,10)
  if abs(x-y) >=2:
    break
  print("too close", x, y)
print(x,y)


x = 20
low = 0
high = x +1
while True:
  if low +1 == high:
    break
  mid = (high + low) // 2
  if mid * mid <=x:
    low = mid
    continue
  high = mid
print(low)
