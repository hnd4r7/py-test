from typing import List

# 1 2 3 3 
# 2
# => 2
class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        # 顺序刷题
        # 数组分成m份, 保证每份的最大值最小.
       
        def can_split(time, day_limit, max_day):
            cur_max = 0
            cur_sum = 0
            used_days = 1
            helper_used = False
            i = 0
            while i < len(time):
                cur_max = max(cur_max, time[i])
                cur_sum += time[i]   # 示例: 1 3 100 1 4
                if cur_sum > day_limit:
                    if not helper_used:
                        cur_sum -= cur_max
                        helper_used = True
                    else:
                        used_days += 1
                        if used_days > max_day:
                            return False
                        cur_sum = 0
                        helper_used = False
                        cur_max = 0
                        i -= 1
                i+=1
            return True

        l, r = 0, sum(time) # 搜索区间 最小值: 从1开始 最大值: 每天刷所有题
        while l <= r:
            mid = (l+r) //2 # 每天刷题量
            if can_split(time, mid, m):
                r = mid-1
            else:
                l = mid+1
        return l

    # def can_split(time: List[int], m: int)
    #     pass

print(Solution().minTime([1,2,3], 3))