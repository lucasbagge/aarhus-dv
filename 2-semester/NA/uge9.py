import numpy as np
import matplotlib.pyplot as plt

print("9.1")

def gram_schmidt(a):
    k = a.shape[1]
    q = np.copy(a)
    r = np.zeros((k,k))
    for i in range(k):
        r[i, i] = np.linalg.norm(q[:, i])
        q[:, i] /= r[i,i]
        r[[i], i+1:] = q[:, [i]].T @ q[:, i+1:]
        q[:, i+1:] -= q[:, [i]] @ r[[i], i+1:]
    return q, r

def least_squares(A, b):
    Q, R = gram_schmidt(A)
    b0 = Q.T @ b
    return np.linalg.solve(R, b0)

x = np.array([0, 1.9, 3.1, 6.2, 7.1])
A = np.array([[1, x[i], x[i]**2] for i in range(len(x))])
y = np.array([1.1, 2.1, 2.9, 4.2, 4.8])

c, b, a = least_squares(A, y)
print("Polynomie koefficienter: a, b,c = ", a, b, c)
X = np.linspace(0, 8, 100)
plt.plot(x, y, "o")
plt.plot(X, c + b*X + a*X**2)
plt.show()


x = np.array([-1.2, -0.3, -0.7, -0.6, 1.6, 1.6, 0.1, 1.5])
y = np.array([0.8, 1.4, -0.8, -0.5, 1.8, -1, -0.7, -1.7])

A = np.array([[2*x[i], 2*y[i], 1] for i in range(len(x))])
b = np.array([x[i]**2 + y[i]**2 for i in range(len(x))])
a, b, c = least_squares(A, b)
r = np.sqrt(c + a**2 + b**2)
print("Cirkel koefficienter: a, b, r = ", a, b, r)
fig, ax = plt.subplots()
circle = plt.Circle((a, b), r)
ax.add_patch(circle)
ax.plot(x, y, "ro")
plt.show()

print()


print("9.2")
iris_dtype = np.dtype([('vals', float, (4,)),('art', np.str_, 16)])
vals, labels = np.loadtxt('iris.data', dtype=iris_dtype,delimiter=',', unpack=True)
iris = vals.T

print("iris.shape: ", iris.shape)
u, s, vt = np.linalg.svd(iris, full_matrices=False)
s = np.diag(s)

svt2 = (s @ vt)[:2]
plt.scatter(*svt2)
plt.show()
for lab in np.unique(labels):
    plt.plot(*(svt2[:, labels == lab]),'o')
plt.show()
