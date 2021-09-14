import time

retries = 0
ex = None

while retries < 3:
    try:
        print(1)
    except Exception as e:
        ex = e
    retries = retries + 1
    time.sleep(2)
if ex is not None:
    raise ex

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    print("11212")


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
