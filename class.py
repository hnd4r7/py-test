import os

'''
Module attributes are writable: you can write modname.the_answer = 42. 
Writable attributes may also be deleted with the del statement. For example, del modname.the_answer 
'''

class class_test:
    def add(self):
        print("sssssssssss")

cls = class_test()
cls.add()
# del cls.add
cls.add()

print("hhh")
# del print
print('hhh')


'''
The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively,
are considered part of a module called __main__, so they have their own global namespace. (The built-in names actually also live in a module; this is called builtins.)
'''

'''
Although scopes are determined statically, they are used dynamically. At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:

the innermost scope, which is searched first, contains the local names
the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
the next-to-last scope contains the current module’s global names
the outermost scope (searched last) is the namespace containing built-in names
'''

'''
The global statement can be used to indicate that particular variables live in the global scope and should be rebound there; the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there.
'''

'''
A special quirk of Python is that – if no global or nonlocal statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data — they just bind names to objects. The same is true for deletions: the statement del x removes the binding of x from the namespace referenced by the local scope. In fact, all operations that introduce new names use the local scope: in particular, import statements and function definitions bind the module or function name in the local scope.
'''

'''
assignments to names always go into the innermost scope!!!
assignments to names always go into the innermost scope!!!
assignments to names always go into the innermost scope!!!
assignments to names always go into the innermost scope!!!
assignments to names always go into the innermost scope!!!
'''

# https://stackoverflow.com/questions/1261875/python-nonlocal-statement
x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


'''
Class definitions, like function definitions (def statements) must be executed before they have any effect. 
(You could conceivably place a class definition in a branch of an if statement, or inside a function.)
'''

class MyClass:
    """A simple example class"""

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    st = 12345

    def f(self):
        return 'hello world'

a = MyClass(2,3)
b = MyClass(4,5)
print(a.__doc__)

'''
a 的属性, 并非class生成的属性了
'''
a.st = 999
print(a.st)
print(b.st)

MyClass.st = 777
print(a.st)
print(b.st)

'''
the special thing about methods is that the instance object is passed as the first argument of the function. 
In our example, the call x.f() is exactly equivalent to MyClass.f(x). 
'''

'''
Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.
'''
a = 1
print(a.__class__)


''' 
Multiple inheritance: depth-first, left-to-right, not searching twice in the same class
'''
class parentA:
    pa = 3
class parentB:
    pb = 4
class child(parentA, parentB):
    c = 5
c1 = child()
print(c1.pa)




















