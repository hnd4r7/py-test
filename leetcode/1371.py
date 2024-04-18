
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mapper = {
            "a": 1,
            "e": 2,
            "i": 4,
            "o": 8,
            "u": 16
        }
        seen = {0: -1}
        res = cur = 0

        for i in range(len(s)):
            if s[i] in mapper:
                cur ^= mapper.get(s[i])
            # 全部奇偶性都相同，相减一定都是偶数
            if cur in seen:
                res = max(res, i - seen.get(cur))
            else:
                seen[cur] = i
        return res

Solution().findTheLongestSubstring("eleetminicoworoep")

# 作者：lucifer
# 链接：https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts/solutions/255035/qian-zhui-he-zhuang-tai-ya-suo-pythonjava-by-fe-lu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。