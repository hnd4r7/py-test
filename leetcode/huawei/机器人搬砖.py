bricks = [int(x) for x in input().split(" ")]
el = sum(bricks) // 8 
er = max(bricks)

if len(bricks) > 8:
    print(-1)
    exit()

bricks.sort(reverse=True)
def check(em):
    hrs = 0
    i = 0
    bts = bricks[:]
    while bts[i] > 0:
        hrs += 1
        bts[i] -= em
        if bts[i] <= 0:
            i+=1
            if i > len(bts)-1:
                break
    return hrs <= 8

while el <= er:
    em = (el+er) // 2
    if check(em):
        er = em-1
    else:
        el = em+1
print(el)
    