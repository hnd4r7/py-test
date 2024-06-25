import collections
import functools

N = int(input())
access = [int(x) for x in input().split(" ")]
threhold = int(input())

cnt = collections.defaultdict(int)
for i in access:
    cnt[i] += 1

print(cnt)
hot = dict(filter(lambda x: x[1] >= threhold, cnt.items()))
print(hot)
ks = list(hot.keys())
ks.sort(key = functools.cmp_to_key(lambda x, y: x - y if hot[x] == hot[y] else hot[y] - hot[x]), reverse = False )

print(len(ks))
for i in ks:
    print(i)