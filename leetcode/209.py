import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre_sum = [0] * len(nums)
        tmp = 0
        for i in range(len(nums)):
            pre_sum[i] = nums[i]+tmp
            tmp += nums[i]
        
        def check(i, j):
            return pre_sum[j] - pre_sum[i-1] >= target if i > 0 else pre_sum[j] >= target

        ans = math.inf
        for i in range(len(nums)):
            l, r = i, len(nums)-1
            while l <= r:
                mid = (l+r) // 2
                if check(i, mid):
                    r = mid-1
                else:
                    l = mid+1
            if l == len(nums):
                continue
            else:
                ans = min(l-i+1, ans)
        return 0 if ans == math.inf  else ans

x = Solution().minSubArrayLen(15, [1,2,3,4,5])
print(x)
        
            
