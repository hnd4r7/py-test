print('"Isn\'t," they said.')
print(r'C:\some\name') 
print(3 * 'xxuu' + "fksdjf")
print('aaa' 'bbb')
text=('abcdefg'
    'kjfslj')
print(text)

print(3 * 'uuu' + 'kjfsklj')

print('abcde'[0])
print('abcde'[-0])
print('abcde'[-1])

print('abcde'[1:3])
print('abcde'[-2:])
print('abcde'[:4])

a='abcde时间'
print(a[:4] + a[4:])

print(len(a))

print(f'{a}kfjsldfj')
print(f"""xxx""""fksdj")

# a[1] = '2' # error

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

s = 'Hello, world.'
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))

import math
print(f'The value of pi is approximately {math.pi:.3f}.')

table  = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!s}.')
print(f'My hovercraft is full of {animals!a}.')
print(f'My hovercraft is full of {animals!r}.s')

print('We are the {} who say "{}!"'.format('knights','Ni'))
print('{1} and {0}'.format('spam', 'eggs'))