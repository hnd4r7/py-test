def my_range(start, end):
    i = start
    while i < end:
        yield i
        i += 1
    
for i in my_range(1,10):
    print(i)

print(sum(my_range(1,20)))


class MyRange:
    def s():
        print(11111111111111)

    def __init__(self,start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.value += 1
        if self.value >= self.end:
            raise StopIteration
        return self.value

MyRange.s()
print(type(MyRange.s))

r = MyRange(1,10)
print("test My Range")
print(next(r))
print(next(r))
print(next(r))

for i in r:
    print(i)

x = map(lambda n: n*n, iter([1, 2, 2, 3]))
print(type(x))
print(all(x))

name = [1,2,2,3]
value = [2,4,6]

print({x:y for x in name for y in value})
print({x:y for x, y in zip(name, value) if x != 2})


print({i for i in range(10)})


#help(MyRange)

print("{:.3f}".format(3.14159));