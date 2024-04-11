import bisect
import collections
import heapq
from bisect import bisect_right
from bisect import bisect_left
from itertools import pairwise
from typing import List

x = [1,2,4,3,4]
print(set(map(sum, pairwise(x))))

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
