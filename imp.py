print("XXXXXXXXXXXXXXXXXimport module codeXXXXXXXXXXXXXXXXXX")
def foo2(name, /, **kwds): #the names of positional-only parameters can be used in **kwds without ambiguity.
    print("foo imported", name)
    return 'name' in kwds