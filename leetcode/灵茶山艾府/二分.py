from bisect import bisect_right
from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # 由于 x 越大 sum 越小，而 key 需要一个增函数（非减），因此对 sum 取相反数从而满足要求
        return bisect_right(range(sum(candies) // k), -k, key=lambda x: -sum(v // (x + 1) for v in candies))

print(Solution().maximumCandies([5,8,6]))

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/solutions/1391104/by-endlesscheng-y031/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。