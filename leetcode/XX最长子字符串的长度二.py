import collections


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

# class Solution:
#     def findTheLongestSubstring(self, s: str) -> int:
#         for i in range(len(s), 0, -1):
#             for j in range(len(s) - i + 1):
#                 sub = s[j:j + i]
#                 has_odd_vowel = False
#                 for vowel in ['a', 'e', 'i', 'o', 'u']:
#                     if sub.count(vowel) % 2 != 0:
#                         has_odd_vowel = True
#                         print("False")
#                         break
#                 if not has_odd_vowel:
#                     print("True")
#                     return  i
#         return 0

# class Solution:
#     def findTheLongestSubstring(self, s: str) -> int:
#         # brute force
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         ans = 0
#         for i in range(len(s)-1, -1, -1):
#             for j in range(0, i):
#                 m = collections.defaultdict(int)
#                 for c in s[j:i]:
#                     if c in vowels:
#                         m[c] += 1
#                 if all(v%2 == 0 for v in m.values()):
#                     ans = max(ans, i-j+1)
#         return ans

x = Solution().findTheLongestSubstring("bcbcbc")
print(x)
