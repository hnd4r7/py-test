a = [1, 2, '2', 4, 1.2, 1]
a[1] = 'fksdljf'
a.append(3)
a[1:3] = [1,1,1]
a[1:3] = []
print(a)


a, b = 0, 1
while a < 10:
    print(a,end=",")
    a, b = b , a + b 
print(a,b)

x = 0
if x:
    print("kfdsjfdlksj")
elif x == 1:
    print("fksdjflks")

users = {'hans': 'active', 'me': 'inactive', 'dude': 'active'}
print(users)
print("hans: ",users['hans'])

for user, status in users.items():
    print(user,status)
    # del users[user] RuntimeError: dictionary changed size during iteration

for user, status in users.copy().items():
    print(user,status)
    del users[user]

print(users)

print(range(1,10))

for i in range(1,100,10):
    print(i)
else:
    print("fsfsfsfsfsfs")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

a = [1]
a.append(2)

class Point:
    x: int
    y: slice

point = {1,2}

# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")

def create_slice():
    result = []
    result.append(1)
    return result

def fib2(n):  # return Fibonacci series up to n
     """Return a list containing the Fibonacci series up to n."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b
     return result

sl = create_slice()
print(sl)

print(fib2(3))

x = [1,2,3]
y = [4,5,6]
# x[len(x):] = [y]
# print(x)
x.append(y)
print(x)
print(x[1:10])
print(x.index(2))

del x[:]
print(x)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4)) # Find next banana starting a position 4
print(fruits.reverse())
fruits.append('grape')
print(fruits)
fruits.sort()
fruits.pop()

x = [None, 'hello', 10]
# x.sort()

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











