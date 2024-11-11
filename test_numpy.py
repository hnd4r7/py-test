import math
from decimal import Decimal, getcontext

import numpy as np

getcontext().prec = 6
print(0.3+0.6 == 0.9)
print(math.fsum((0.3, 0.6)) == 0.9)
print(float(Decimal(0.3) + Decimal(0.6)) == float(Decimal(0.9)))
print(Decimal("0.3") + Decimal("0.6") == Decimal("0.9"))

m1 = np.array([[2, 3], [-1, -3]])
m2 = np.array([[5, 0], [-2, 1]])
print(np.matmul(m1, m2))

a = np.array([[3, 1], [1, 2]])
# b = np.array([[0, 1], [1, 0]])
b = np.array([[1, 2], [3, 4]])
print(np.matmul(a, b))

x = np.array([1, -2, -5])
y = np.array([4, 3, -1])
print(np.matmul(x, y))

try:
    np.matmul(x.reshape((3, 1)), y.reshape((3, 1)))
except ValueError as err:
    print(err)

print(np.zeros((3, 2)))


a = np.array([[0,0,1], [2,2,1], [1,0,0]])
print(np.linalg.det(a))
print(a.transpose())

s = np.array([0,1,2,3,4])
print(s.shape)
print(s.transpose().shape)
