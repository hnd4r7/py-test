import collections
from heapq import *
from bisect import bisect_right
from bisect import bisect_left
from itertools import pairwise
from collections import Counter
import itertools
import math
import string
from typing import List

"""
123
384
535
"""

print(True+True)

exit()
x = [1,2,4,3,4]
print(set(map(sum, pairwise(x))))

s = sorted([2,1,3], key = lambda x: x)
print(s)

float('inf')
float(math.inf)

def x()->bool:
    return False

class Node:
    def __init__(self,val):
        self.val = val
    
Node.__lt__ = lambda a, b: a.val < b.val    

n = Node(3)
n2 = Node(4)
print(n > n2)

x = int("8f", 16)
print(x)

a = [[]] + [[]] + [[]] 
a[0].append(1)
print(a)


a = [[]] * 4
a[0].append(1)
print(a)

a[0].append('2')
print(type(a[1]))
print(a)
exit()

a = {(1,2)}
print(type(a))
exit()

x = -1
print(3 + -x)
exit()

heapq.heapify()
r = [4,4,2,4,4]
x = Counter(r).items()
print(x)
for a, b in x:
    print(a, b)

print(max(Counter(r).values()))

print('aba' == 'aba')

q = collections.deque((7, 1))
x = q.popleft()
print(x)

x = "32111888888"
y = sorted(range(10), key = lambda i: x[i], reverse= True)
print(y)

string.ascii_lowercase

x = "123"
x = x[1:]
print(x)



def compressString(self, S: str) -> str:
       return min( S, "".join(k + str(len(list(grp))) for k, grp in itertools.groupby(S)), key=len)

for k, g in itertools.groupby("aabcccccaaa"):
    print(list(g))

x = [[1,2],[3,5],[6,7],[6,10],[12,16]]
y = [6,8]

x = [1,2,5]
print(bisect_left(x,5))
exit()

for i in range(len(x)):
    print(i)
    if i==1:
        i-=1
exit()

def find(nums: List[int], x: int):# -> tuple[int, int]:
    l, r = 0, len(nums)-1
    while l <= r: # 闭区间搜索区间判定条件是
        mid = (l+r)//2
        if nums[mid] > x:
            r = mid
        else:
            l = mid+1
    return nums[l], nums[r]

def find(nums: List[int], x: int):# -> tuple[int, int]:
    l, r = 0, len(nums)
    while l < r: # 搜索区间判定条件是
        mid = (l+r)//2
        if nums[mid] > x:
            r = mid
        else:
            l = mid+1
    return nums[l], nums[r]

l, r = find(x, 8)
print(l, r)
exit()


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
         # 由于 x 越大 sum 越小，而 key 需要一个增函数（非减），因此对 sum 取相反数从而满足要求
        return bisect_right(range(sum(candies) // k), -k, key=lambda x: -sum(v // (x + 1) for v in candies))

class Node:
    pass

a = Node()
b = a
print(b is a )

x = set()
x.add(1)

print(1 in x)

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
