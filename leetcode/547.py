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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 110 100
        # 110 010
        # 001 001
        # dfs
        """
        ans = 0
        visited = set()

        def dfs(i):
            if len(isConnected[i]) == 0:
                return
            for x in range(len(isConnected[i])):
                if isConnected[i][x] == 1 and x not in visited:
                    visited.add(x)
                    dfs(x)
            
            
        for i in range(len(isConnected)):
            if i in visited:
                continue
            ans += 1
            visited.add(i)
            dfs(i)

        return ans
        """
        # union find
        par = [i for i in range(len(isConnected[0]))]

        def find(x):
            if par[x] != x:
                return find(par[x])
            else:
                return x
        def union(x, y):
            par[find(x)] = find(y)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    union(i, j)
        return len(Counter(par).keys())

Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])



