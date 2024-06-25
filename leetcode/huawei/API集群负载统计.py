import collections

log_count = int(input())
logs = [input() for _ in range(log_count)]
level, q = input().split(" ")
ql = int(level)

m = collections.defaultdict(dict) # level: kw: cnt

ans = 0
for l in logs:
    kw = l.split("/")
    # if len(kw) < level:
    #     continue
    # if q == kw[level]:
    #     ans += 1
    for level, w in enumerate(kw):
        if w in m[level]:
            m[level][w] += 1
        else:
            m[level][w] = 1
print(m)

if ql not in m:
    print(0)

print(m[ql][q])
