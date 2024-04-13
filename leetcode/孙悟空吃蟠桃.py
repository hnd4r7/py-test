ps = list(map(int, input().split(" ")))
time = int(input())

if time < len(ps):
    print(0)
    exit()
if time == len(ps):
    print(max(ps))
    exit()

def check():
    pass #TODO

l, r = 0, max(ps)
while l < r:
    mid = (l+r)//2
    if check(mid):
        r = mid -1
    else:
        l = mid+1
print(l)