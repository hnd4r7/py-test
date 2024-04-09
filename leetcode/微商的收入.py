import collections

"""
3
1 0 223
2 0 323 
3 2 1203
"""

n = int(input())
deles = [[int(x) for x in input().split(" ")] for _ in range(n)]
print(deles)

deles.sort(key = lambda x: (x[1],x[0]), reverse = True)

print(deles)
# last_money = 0

top = deles[-1][1]

# sub = collections.defaultdict(list)

# dele_set = set()

# for d in deles:
#     sub[d[1]].append(d[0])
#     dele_set.add(d[0])

money = collections.defaultdict(int)

for d in deles:
    money[d[0]] += d[2]
    money[d[1]] += money[d[0]] //(100 *15)

print(money)
print(money[top])
