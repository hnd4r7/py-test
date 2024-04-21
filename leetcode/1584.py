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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        points = [(x,y) for x, y in points]
        N = len(points)
        # dis = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(i+1, N):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[points[i]].append((points[j], dis))
                adj[points[j]].append((points[i], dis))

        vis = set()
        cost = 0
        h = [(0, points[0])]
        while h:
            dis, i = heappop(h)
            if i in vis:
                continue
            vis.add(i)
            cost += dis
            for j, nd in adj[i]:
                if j not in vis:
                    heappush(h, (nd, j))
        return cost


print(Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))