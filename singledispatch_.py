from functools import singledispatch

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

@fun.register
def _(arg: int, verbose=False):
    print("Strength in numbers, eh?", end=" ")

@fun.register
def _(arg: list, verbose=False):
    print("hhhhhhhhhhhhhhhhhhhhh")

fun([1,2], verbose = True)
fun(3, verbose = True)