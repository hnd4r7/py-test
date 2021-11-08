
"""
Important warning: The default value is evaluated only once.
 This makes a difference when the default is a mutable object such as a list, dictionary, 
 or instances of most classes. For example, 
 the following function accumulates the arguments passed to it on subsequent calls:
"""

def f(a, L=[]):
    L.append(a)
    return L

"""
https://stackoverflow.com/questions/13087344/python-function-default-parameter-is-evaluated-only-once
Noted: Python passes parameters to functions by value; So for objects, the value passed is a reference to the object, not a new copy of the object.
"""

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print(f2(1))
print(f2(2))
print(f2(3))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument
parrot(voltage=1000)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def foo(name, **kwds):
    return 'name' in kwds

# foo(1, **{'name': 2})
# print(foo(1,name = 2))

def foo2(name, /, **kwds): #the names of positional-only parameters can be used in **kwds without ambiguity.
    return 'name' in kwds

print(foo2(1, **{'name': 2}))
print(foo2(1,name = 2))


args = [3, 6]
print(list(range(*args))) #unpacking list
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d) #unpacking dict

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(3))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

def my_function():
     """Do nothing, but document it.

     No, really, it doesn't do anything.
     """
     pass
print(my_function.__doc__)

def f(ham: str, eggs: str = 'eggs') -> str:
     print("Annotations:", f.__annotations__)
     print("Arguments:", ham, eggs)
     return 2
    #  return ham + ' and ' + eggs
f('spam')
print(f('jh','jkj'))
