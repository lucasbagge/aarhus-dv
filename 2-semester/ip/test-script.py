# min plot from scipy
from math import sin
import matplotlib.pyplot as plt
from scipy.optimize import minimize

trace= []  # remember calls to f
def f(x):
    value = x ** 2 + 10 * sin(x)
    trace.append((x, value))
    return value
X = [-8 + 18 * i / 9999 for i in range(1000)]
Y = [f(x) for x in X]

plt.style.use("dark_background")
plt.plot(X,Y, "-w")
for start, color in [(8, 'red'), (-6, 'yellow')]:
    trace = []

    solution = minimize(f, [start], method = "nelder-mead")

    x, y = solution.x[0], solution.fun
    
    plt.plot(*zip(*trace), '.-', c = color, label = f'start {start:.1f}')
    plt.plot(*trace[0], 'o', c = color)
    plt.text(x, -23, f'{x:.3f}', c = color, ha = 'center')
    plt.plot([x,x], [-18,y], '--', c = color)
plt.xticks(range(-5, 15, 5))
plt.yticks(range(-25, 100, 25))
plt.minorticks_on()
plt.legend()
plt.show()

