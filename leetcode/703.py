import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = [0-x for x in nums]
        self.k = k
        heapq.heapify(nums)
        self.h = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.h, 0-val)
        def dfs(n):
            min_num = heapq.heappop(self.h)
            n -= 1
            if n == 0:
                heapq.heappush(self.h, min_num)
                return min_num
            ans = dfs(n)
            heapq.heappush(self.h, min_num)
            return ans
        return 0-dfs(self.k)

# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
x = KthLargest(3, [4,5,8,2])
print(x.add(3))
print(x.h)
print(x.add(5))
print(x.h)
print(x.add(10))
print(x.h)
print(x.add(9))
print(x.h)
print(x.add(4))
print(x.h)
