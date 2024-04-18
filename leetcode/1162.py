from collections import deque
from functools import cache
from math import inf
from typing import List


# class Solution:
#     def maxDistance(self, grid: List[List[int]]) -> int:
#         directions = [(-1,0), (1,0), (0,-1), (0,1)]
#         v = set()
#         @cache
#         def dfs(i,j):
#             if i <0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
#                 return inf
#             if grid[i][j] == 1:
#                 return 0
#             ans = inf
#             for d in directions:
#                 if (i+d[0], j+d[1]) in v:
#                     continue
#                 v.add((i+d[0], j+d[1]))
#                 ans = min(ans, 1+dfs(i+d[0], j+d[1]))
#                 v.remove((i+d[0], j+d[1]))
#             print(v)
#             return ans
            
#         ans = -inf
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 0:
#                     res = dfs(i, j)
#                     ans = max(ans, res) if res != inf else ans
#         return ans if ans != -inf else -1

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        # v = set()
        # def dfs(i,j):
        #     if i <0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        #         return inf
        #     if grid[i][j] == 1:
        #         return 0
        #     ans = inf
        #     for d in directions:
        #         if (i+d[0], j+d[1]) in v:
        #             continue
        #         v.add((i+d[0], j+d[1]))
        #         ans = min(ans, 1+dfs(i+d[0], j+d[1]))
        #         v.remove((i+d[0], j+d[1]))
            
        #     return ans
            
        # ans = -inf
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 0:
        #             res = dfs(i, j)
        #             v = set()
        #             ans = max(ans, res) if res != inf else ans
        # return ans if ans != -inf else -1

        # dfs无法cache 因为中间可能出现绕路走的情况, bfs稳扎稳打比较适合.
        
        
        def check_idx(i, j):
            return not (i <0 or j < 0 or i >= len(grid) or j >= len(grid[0]))

        def max_dis(x, y):
            q = deque([(x, y)])
            while q:
                for i in range(len(q)):
                    cur = q.popleft()
                    for d in directions:
                        nx = cur[0] + d[0]
                        ny = cur[1] + d[1]
                        if not check_idx(nx, ny):
                            continue
                        if grid[nx][ny] == 1:
                            return abs(nx-x) + abs(ny-y)
                        else:
                            q.append((nx,ny))
            return -inf

        ans = -inf
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                   print(i,j, max_dis(i, j))
                   ans = max(ans, max_dis(i, j))
        
        return ans
        
# Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])
# Solution().maxDistance([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
print(Solution().maxDistance([[1,0,0],[0,0,0],[0,0,0]]))
