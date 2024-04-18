import functools
import math
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.sort()
        n = len(days)

        @functools.cache
        def dfs(day_idx):
            if day_idx > n-1:
                return 0
            if day_idx == n-1:
                return costs[0]
            def cal_idx(start, valid_days):
                i = start
                while i < n-1 and days[i] - days[start] < valid_days:
                    i+=1
                return n-1 if days[i] - days[start] == valid_days else math.inf
            buy_1_day = costs[0] + dfs(day_idx+1)
            buy_7_day = costs[1] + dfs(cal_idx(day_idx,7))
            buy_30_day = costs[2] + dfs(cal_idx(day_idx, 30))
            return min(buy_1_day, buy_7_day, buy_30_day)

        return dfs(0)

Solution().mincostTickets([1,4,6,7,8,20], [2,7,15])
