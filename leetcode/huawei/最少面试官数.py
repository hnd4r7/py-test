import collections
from heapq import *
from bisect import bisect_right
from bisect import bisect_left
from itertools import pairwise
from collections import Counter
import itertools
import string
from typing import List

# m = 2 #每名面试官最多面试m场.
# interviews = [[1,2], [2,3], [3,4], [4,5],[5,6]]

m = 3 #每名面试官最多面试m场.
interviews = [[8,35], [5,10], [1,3]]

interviews.sort()

total = 0

# 1-5 
# 2-4
q = [(0, 0)] # 下次开始面试的时间, 已经面试的次数

used = 0
for i in interviews:
    start, end = i[0], i[1]
    if not q:
        heappush(q, (0,0))
    next_valid_time, cnt = q[0]
    if next_valid_time > start:
        heappush(q, (end, 1))
    if next_valid_time <= start: 
        if cnt == m:
            used+=1
            heappop(q)
        else:
            heappop(q)
            heappush(q, (end, cnt+1))
print(len(q)+used)
    
    
    
    
    