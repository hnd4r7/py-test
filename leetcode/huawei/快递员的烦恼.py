import collections
import math

"""
2 1
1 1000
2 1200
1 2 300
-> 2500

5 1
5 1000
9 1200
17 300
132 700
500 2300
5 9 400
-> 9200
"""

n, m = [int(x) for x in input().split(" ")]
e_dis = [[int(x) for x in input().split(" ")] for _ in range(n)]
edis_m = {}
for k, v in e_dis:
    edis_m[k] = v

# c_dis = [{int(x): (int(y), int(z)) for x, y, z in input().split(" ")} for _ in range(1)]
c_dis = [[int(x) for x in input().split(" ")] for _ in range(m)]
c_dis_m = collections.defaultdict(lambda: [])

for x, y, cost in c_dis:
    c_dis_m[x].append((y, cost))
visited = set()

min_dis = math.inf
def dfs(cur, dis):
    global min_dis
    if len(visited) == len(e_dis):
        min_dis = min(min_dis, dis + edis_m[cur])
        return

    if cur in c_dis_m:
        for x,cost in c_dis_m[cur]:
            if x not in visited:
                visited.add(x)
                dfs(x, dis+cost)
                visited.remove(x)

    for k, v in edis_m.items():
        if k not in visited:
            visited.add(k)
            dfs(k, dis+v+edis_m[cur])
            visited.remove(k)

for k, v in edis_m.items():
    visited.add(k)
    dfs(k, v)
    visited.remove(k)

print(min_dis)