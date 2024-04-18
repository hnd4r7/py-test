import collections
from heapq import *
from bisect import bisect_right
from bisect import bisect_left
from itertools import pairwise
from collections import Counter
import itertools
import string
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # dfs 超时了
        m, n = len(heights), len(heights[0])
        if m == n and n == 1:
            return 0
        # visited = []
        # @cache
        # def dfs(i, j, max_h):
        #     if i == m-1 and j == n-1:
        #         print(max_h, [heights[x][y] for x,y in visited])
        #         return max_h
        #     ans = inf
        #     for ni, nj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
        #         if not (0<=ni<m and 0<=nj<n):
        #             continue
        #         if (ni, nj) in visited:
        #             continue
        #         visited.append((ni, nj))
        #         ans = min(ans, dfs(ni, nj, max(max_h, abs(heights[ni][nj] - heights[i][j]))))
        #         visited.pop()
        #     return ans
        # return dfs(0,0,-inf)

        # bfs + 二分
        # l, r = 0, 10**6-1
        # def check(mid):
        #     q = collections.deque([(0,0)])
        #     visited = [[False] * n for _ in range(m)]  # 二维数组加速.
        #     visited[0][0] = True
        #     while q:
        #         for _ in range(len(q)):
        #             i, j = q.popleft()
        #             for ni, nj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
        #                 if not (0<=ni<m and 0<=nj<n):
        #                     continue
        #                 if visited[ni][nj]:
        #                     continue
        #                 if abs(heights[ni][nj] - heights[i][j]) > mid:
        #                     continue
        #                 if ni == m-1 and nj == n-1:
        #                     return True
        #                 q.append((ni,nj))
        #                 visited[ni][nj] = True
        #     return False

        # while l <= r:
        #     mid = (l+r)//2
        #     if check(mid):
        #         r = mid -1
        #     else:
        #         l = mid + 1
        # return l

        # 优先级队列
        q = [(0, 0, 0)]
        visited = {(0, 0)}
        while q:
            dis, i, j = heappop(q)  # 在每个点上记录之前到现在的最大height差,  详细查看: https://www.youtube.com/watch?v=XQlxCCx2vI4
            if i == m - 1 and j == n - 1:
                return dis
            if (i,j) in visited:
                continue
            visited.add((i, j))
            for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if (ni, nj) in visited:
                    continue
                new_dis = max(dis, abs(heights[ni][nj] - heights[i][j]))
                print(ni, nj)
                heappush(q, (new_dis, ni, nj))
        return -1

        # m, n = len(heights), len(heights[0])
        # visit = set()
        # nodes = [(0, 0, 0)]  # dis, i, j
        # while nodes:
        #     dis, i, j = heapq.heappop(nodes)
        #     if i == m - 1 and j == n - 1:
        #         return dis
        #     if (i, j) in visit:  # 跳过已经遍历过的点
        #         continue
        #     visit.add((i, j))
        #     for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        #         if 0 <= x < m and 0 <= y < n and (x, y) not in visit:
        #             heapq.heappush(nodes, (max(dis, abs(heights[x][y] - heights[i][j])), x, y))

Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])