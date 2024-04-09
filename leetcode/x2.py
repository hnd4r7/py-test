import collections
import math
from typing import List

x = [1,2,3,4]
x = math.inf
print(type(x))

# n = int(input())
# ans = 0
# for _ in range(n):
#     p, q = list(map(int, input()))
#     if q-p >= 2:
#         ans += 1
# print(ans)

x = [1,2,3,4] # y= x[::-1]
for i in range(len(x)):
    x[i] -= 1
print(x)
exit()

x = []
y = x[0] if len(x) > 0 else 0
print("xxxxxxxxxxxxxxxxxxxxxxxx", y)




# 
# 
# class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row = [[x for x in y if x != '.'] for y in board]
        # print(row)
        # col = [[x for x in y if x != '.'] for y in zip(*board)]
        # print(col)
        # pal = [[board[i+m][j+n] for m in range(3) for n in range(3) if board[i+m][j+n] != '.'] for i in (0, 3, 6) for j in (0, 3, 6)]
        # print(pal)
        # for x in (*row, *col, *pal):
            # print(x)
        # return all(len(set(x)) == len(x) for x in (*row, *col, *pal))
# 
# b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Solution().isValidSudoku(b)


# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         nums = [float('-inf')] + nums + [float('-inf')]
#         l, r = 0, len(nums)-1
#         while l <= r:
#             m = l + (r-l)//2
#             if nums[m] > nums[m+1] and nums[m] > nums[m-1]:
#                 return m-1
#             elif nums[m] < nums[m+1] and nums[m] > nums[m-1]:
#                 l = m+1
#             elif nums[m] > nums[m+1] and nums[m] < nums[m-1]:
#                 r = m-1
#         return -1


# Solution().findPeakElement([3, 2, 1])
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = collections.defaultdict(int)
        for c in tasks:
            cnt[c] += 1
        
        print(cnt)
        print(list(cnt.keys()))

        ks = list(cnt.keys())
        ks.sort(key= lambda x: cnt[x], reverse=True)

        wait = collections.defaultdict(int)
        time = 0
        while True:
            time_elapsed = 0
            i = 0
            while i < len(ks): 
                if cnt[ks[i]] <=0:
                    i+=1
                    continue
                c = ks[i]
                if c not in wait or time - wait[c] >= n:
                    cnt[c] -= 1
                    time_elapsed += 1
                    # reverse to initial char
                    time += 1
                    wait[c] = time
                if time_elapsed == n+1:
                    time_elapsed = 0
                    i = 0
                else:
                    i += 1
            if all(x == 0 for x in cnt.values()):
                return time
            if time_elapsed < n+1:
                time += n+1-time_elapsed
    
    def leastInterval2(self, tasks: List[str], need: int) -> int:
        n, c = len(tasks), collections.Counter(tasks)
        most = c.most_common()
        first_freq, cnt = most[0][1], 1
        for i in range(1, len(most)):
            if most[i][1] == first_freq: cnt += 1
        res = (first_freq - 1) * (need+1) + cnt 
        return res if res >= n else n

    def leastInterval3(self, tasks: List[str], n: int) -> int:
        ct = collections.Counter(tasks)
        nbucket = ct.most_common(1)[0][1]
        print(ct.values())
        print(list(ct.values()).count(6))
        last_bucket_size = list(ct.values()).count(nbucket)
        res = (nbucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))

print(Solution().leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2))

x = {1:2}
print(2 not in x)

for c, v in x.items():
    print(c, v)


#for i in range(10):
i = 0
while i < 10:
    i += 2
    print(i)

x = [1,2,3,4]
x.insert(0,8)
x.reverse()
print(x)

print("ssss, ".join(map(str, x)))

y = sorted(x)