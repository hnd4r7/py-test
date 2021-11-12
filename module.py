
"""
import modules
"""

print("-"*100)
print("current name: ", __name__)

import imp 
print(imp.foo2("aaa",aa = 'bb',cc ='dd',ee= 'ff'))
print("imp's name::::",imp.__name__)

from imp import foo2 
foo2('ccc')

def foo2(name):
    print("foo current" , name)
    global sys
    import sys

foo2('ddd')
foo2 = imp.foo2
print(sys.path)

import builtins
print(dir(builtins))

