import collections
N = int(input())
conns = collections.defaultdict(set)
hs = set()
for _ in range(N):
    h1, h2 = input().split(' ')
    conns[h1].add(h2)
    hs.add(h1)
    hs.add(h2)

for h in hs:
    for o in conns[h]:
        if h not in conns[o]:
            print(False)
            exit()
print(True)

