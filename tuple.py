t = 1, 2, 'aa', 'b', ('a','b','c','d')
print(t[4][2])

l = [1,2,3,4]

"""
tuples can not be changed while list can, but list occupy more mem space than tuple
"""

print(dir(t))
print(80*'-')
print(dir(l))

import sys
print(dir(sys))
# print(help(sys.getsizeof))

d1 = [1,2,3,4]
d2 = 1,2,3,4
print(sys.getsizeof(d1))
print(sys.getsizeof(d2))

unpacking = 1,2,3
x, y, z = unpacking
print(x,y,z)

import timeit
time_test = timeit.timeit(stmt="print('sll')",number=10)
list_test = timeit.timeit(stmt="[1,2,3,4,5]",number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)",number=1000000)
print(list_test)
print(tuple_test)