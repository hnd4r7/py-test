from math import inf
from typing import List
# BFS

# https://renjie.blog.csdn.net/article/details/135299078


"""
123
456
789
"""

def cal_time(lights: List[List[int]], time_per_period: int, row_start: int, col_start: int, row_end: int, col_end: int):
    m, n = len(lights), len(lights[0])
    visited = set()
    def dfs(i, j, last_dir):
        if i == row_end and j == col_end:
            print(visited)
            return 0
        min_time = inf
        for direction in [(-1,0),(0,-1),(1,0),(0,1)]:
            ni, nj = i+direction[0], j+direction[1]
            if ni< 0 or ni >= m or nj <0 or nj >=n:
                continue
            if direction[0] == -last_dir[0] and direction[1] == -last_dir[-1]: #回头情况
                continue
            if (ni, nj) in visited:
                continue
            time = 0 
            if not (direction[0] == -last_dir[1] and direction[1] == -last_dir[0]): # 右转情况
                try:
                    time += lights[ni][nj]
                except:
                    print(ni, nj)
            visited.add((ni,nj))
            print(direction)
            time = time_per_period + dfs(ni, nj, direction)
            min_time = min(min_time, time)
            visited.remove((ni,nj))
        return min_time
    return dfs(row_start, col_start, (0,1))
print(cal_time([[1,2,3],[4,5,6],[7,8,9]],60,0,0,2,2))