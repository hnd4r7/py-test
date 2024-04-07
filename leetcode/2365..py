import collections
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        if len(tasks) <= 1: return 1
        days = 0
        wait = collections.defaultdict(int)
        for i in range(len(tasks)):
            tt = tasks[i]
            passed = 0
            if tt not in wait or wait[tt] == 0:
                passed = 1
            else:
                passed = wait[tt] + 1
            for k, v in wait.items():
                if v - passed <= 0:
                    wait[k] = 0
                else:
                    wait[k] = v-passed
            days += passed
            wait[tt] = space
        return days

x = Solution().taskSchedulerII([5,8,8,5], 2)
print(x)