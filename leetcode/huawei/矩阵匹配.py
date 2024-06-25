print(2**4)
a, *b = 1, 1, 2, 3
print(a, b)

# n, m, k = map(int, input().split(" "))
# matrix = [0] * n
# for i in range(n):
#     matrix[i] = list(map(int, input().split(" ")))

# for i in matrix:
#     print(' '.join(i))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ans = 0, 0, 1
        while l <= r and r < len(s):
            r += 1
            while s[r] in s[l:r+1]:
                l += 1
            ans = max(ans, r-l+1)
        return ans

print(Solution().lengthOfLongestSubstring("pwwkew"))

import collections
cnt = collections.Counter()