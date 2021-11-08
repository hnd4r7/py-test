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