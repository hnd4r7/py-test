import collections
# 前缀和 + 状态压缩


# s = input()
# cs = ['l', 'o', 'x']

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(s), 0, -1): # 从最长长度开始遍历.
            for j in range(0, len(s)-i+1):
                m = collections.defaultdict(int)
                for c in s[j:i+j]:
                    if c in vowels:
                        m[c] += 1
                if all(v%2 == 0 for v in m.values()):
                    return i
        return 0
x = Solution().findTheLongestSubstring("bcbcbc")
print(x)
