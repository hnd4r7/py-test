import collections
n = input()
input_arr = [int(x) for x in input().split(" ")]
graph = collections.defaultdict
for i in range(len(input_arr)-1):
    graph[input_arr[i]].append(input_arr[i+1])
visited = []
end = []
def dfs(i, path):
    if i not in graph:
        end.append(i)
    for t in graph[i]:
        if t in path:
            print(-1)
            exit()
        path.add(t)
        dfs(t)
        path.remove(t)
dfs(0, {})
# 入度为0