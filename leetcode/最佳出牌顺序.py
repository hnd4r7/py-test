from collections import Counter
from math import inf


cards = [3,3,4,5,6,7,7]
cs = Counter(cards)
ck = list(cs.keys())
ck.sort()
n = len(ck)

# https://renjie.blog.csdn.net/article/details/131948426
def cal_diff(l, r):
    benefit = 0
    for i in range(l, r+1):
        if cs[ck[i]] == 1:
            benefit += ck[i]
        if cs[ck[i]] == 2:
            benefit -= ck[i] #对子是 x * 4 顺子是 x * 2 + x 
        elif cs[ck[i]] == 3:
            continue
        elif cs[ck[i]] == 4:
            benefit -= 4 * ck[i] # 炸弹是 4 * 3 * x 拆开是 3 * 2 * x + 2 * x
    return benefit


l, r = 0,1 # 连续滑动窗口, 最大连续长度里面, 判断里面差值最大的情况. 然后再扫描一遍, 直到没有顺子为止.
ml, mr, max_diff = 0, 0, -inf

score = 0
while True:
    #TODO: ck[r+4] - ck[r] = 4 即可知道这几个key是连续的. 中间要删除cnt是0的key
    while l <= r and r < n:
        if ck[r] - ck[r-1] == 1 and cs[ck[r]] > 0:
            r+=1
        else:
            r+=1
            l=r
        if r - l + 1 >= 5:
            d = cal_diff(l, r)
            if d > max_diff:
                ml, mr, max_diff = l, r, d
            l+=1
            r+=1

    if max_diff > 0: # 顺子好处
        # 出顺
        for i in range(l-1, r):
            cs[ck[i]] -= 1
            score += ck[i] * 2
        # 重置l和r
        l,r,max_diff = 0,1,-inf
    else:
        break

# 算出最后差值
for k, v in cs.items():
    if v == 2:
        score += k * 2 * 2
    elif v == 3:
        score += k * 3 * 2
    elif v == 4:
        score += k * 4 * 3
    elif v == 1:
        score += k
print(score)

