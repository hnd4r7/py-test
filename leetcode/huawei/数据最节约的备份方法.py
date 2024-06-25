datas = [int(x) for x in input().split(",")]
l, r = 0, len(datas)

def check(buckets_num):
    buckets = [0] * buckets_num
    datas.sort(reverse=True)

    for d in datas:
        buckets.sort()
        buckets[0] += d
        if buckets[0] > 500:
            return False
    return True
    

while l <= r:
    mid = (l+r)//2
    if check(mid):
        r = mid-1
    else:
        l = mid+1
print(l)