import collections


task_deps = [x for x in input().split(" ")]
indegrees = collections.defaultdict(int)
graph_ord = collections.defaultdict(list)

courses = set()
for t in task_deps:
    a, b = t.split("->")
    indegrees[a] += 1
    graph_ord[b].append(a)
    courses.add(a)
    courses.add(b)

q = [c for c in courses if c not in indegrees]

visited = set()

while q:
    tmp = []
    for i in range(len(q)):
        c = q.pop()
        if c not in visited:
            print(c)
            visited.add(c)
            tmp.append(c)
    for c in tmp:
        for nc in graph_ord[c]:
            q.append(nc)



