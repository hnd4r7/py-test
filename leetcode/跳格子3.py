from functools import cache
import math


score = [1, -1,-6, 7, -17, 7]
k = 2
n = len(score)

# dp[n-1] = dp[n-1-k] + max(score[n-1-k:n-1]) 

@cache
def dfs(i):
    global ans
    if i == n-1:
        return score[n-1]
    m = -math.inf
    for step in range(1, k+1):
        if i+step > n-1:
            continue
        m = max(dfs(i+step) + score[i],m)
    return m
print(dfs(0))