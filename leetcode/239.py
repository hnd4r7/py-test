import heapq
from typing import List

max(1,2)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = [0] * len(temperatures)
        # 递增的单调栈
        for i, v in enumerate(temperatures):
            while len(s) > 1 and v > s[len(s)-1][1]:
                ans[s[len(s)-1][0]]=i-s[len(s)-1][0]
                s.pop()
            s.append((i, v))
        return ans


print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x > y:
                heapq.heappush(stones,x-y)
        if not stones:
            return 0
        else:
            return stones[0]

print(Solution().lastStoneWeight([2,7,4,1,8,1]))