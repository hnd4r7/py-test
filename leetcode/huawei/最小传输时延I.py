import collections
import math

"""
3 3
1 2 11
2 3 13
1 3 50
1 3
"""

node_cnt, time_cnt = [int(x) for x in input().split(" ")]
times = [[int(x) for x in input().split(" ")]  for _ in range(time_cnt)]
start_node, end_node = [int(x) for x in input().split(" ")]

graph = collections.defaultdict(list)
for t in times:
    graph[t[0]].append((t[1], t[2]))

min_cost = math.inf

def dfs(node, cur_cost):
    global end_node, min_cost
    if node == end_node:
        min_cost = min(cur_cost, min_cost)
    for ts in graph[node]:
        next_node = ts[0]
        cost = ts[1]
        dfs(next_node, cur_cost+cost)

dfs(start_node, 0)
print(min_cost)


