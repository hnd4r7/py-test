
"""
list comp:
"""

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print([(x, x**2) for x in range(6)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])
print([[row[i] for row in vec] for i in range(3)])

del(vec[:])
print(vec)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)

l = ['tic', 'tac', 'toe']
for i, v in enumerate(l):
    print(i,v)
for v in l:
    print(v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0} ? It is {1}'.format(q, a))


for i in reversed(l):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'banana']
for i in sorted(basket):
    print(i)


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)