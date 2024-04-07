import collections
import heapq

x = [2, 3, 1, 4, 5]
y = [10,20,30]
heapq.heapify(x)
print(x)

heapq.heappop

print(True > 0)
print(False == 0)
print(False < 0)

q = collections.deque()
q.append(1)
print(q)

a = "s"
if a: print("xkjklfsjdf")

x = [1,2,3,4]
import functools

x.sort(key=functools.cmp_to_key(lambda x, y: y-x))
# x.sort(compare_to_key = lambda x, y: x - y)
print(x)

y = functools.reduce(lambda x, y: x + y, x, 10)
print(y)
