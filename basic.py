"""
https://docs.python.org/3/library/stdtypes.html#truth-value-testing

Truth Value Testing
Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a __bool__() method that returns False or a __len__() method that returns zero, when called with the object. 1 Here are most of the built-in objects considered false:

constants defined to be false: None and False.

zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

empty sequences and collections: '', (), [], {}, set(), range(0)

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)
"""

l = [1,2,3]
if l:
    print("fksdjfksj")

del l[:]

if l:
    print("ffff")
else:
    print("ttttt")


string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)


from cal import * 

# import os as _os, sys as _sys
import os
print(os.name)