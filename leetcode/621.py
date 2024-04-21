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
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # cnt = collections.defaultdict(int)
        # for c in tasks:
        #     cnt[c] += 1

        # ks = list(cnt.keys())
        # ks.sort(key=lambda x: cnt[x], reverse=True)

        # wait = collections.defaultdict(int)
        # time = 0
        # while True:
        #     time_elapsed = 0
        #     i = 0
        #     while i < len(ks):
        #         if cnt[ks[i]] <= 0:
        #             i += 1
        #             continue
        #         c = ks[i]
        #         if c not in wait or time - wait[c] >= n:
        #             cnt[c] -= 1
        #             time_elapsed += 1
        #             # reverse to initial char
        #             time += 1
        #             wait[c] = time
        #         if time_elapsed == n:
        #             time_elapsed = 0
        #             i = 0
        #         else:
        #             i += 1
        #     if all(x == 0 for x in cnt.values()):
        #         return time
        #     if time_elapsed < n + 1:
        #         time += n + 1 - time_elapsed
        h = [-x for x in Counter(tasks).values()]
        heapify(h)
        q = []
        time = 0
        while q or h:
            if h:
                v = heappop(h)
                if v+1 >= 0:
                    continue
                heappush(q, (time+n, v+1))
            # elif q:
            #     if time > q[0][0]:
            #         waiting = heappop(q)
            #         if waiting[1]+1 == 0:
            #             continue
            #         heappush(q, (time+n, waiting[1]+1))
            while q:
                # 加入工作队列, 等待下次time的时候pop
                if time >= q[0][0]:
                    waiting = heappop(q)
                    heappush(h, waiting[1])

            time += 1
            print(time,h,q)
        return time

Solution().leastInterval(["A","A","A","B","B","B"], 2)
# Solution().leastInterval(["A","C","A","B","D","B"], 1)