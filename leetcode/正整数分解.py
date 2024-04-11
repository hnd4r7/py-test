# https://blog.csdn.net/2301_76848549/article/details/134854803
import math
n = int(input())
l, r = 0,0 
total = 0
ans = math.inf
while r <= n:
    if total < n:
        r+=1
        total += r
    elif total > n:
        l+=1
        total -= l
    elif total == n:
        ans = min(ans, r-l+1)
        r+=1
        l+=1
        total -= l
        total += r

print(ans)