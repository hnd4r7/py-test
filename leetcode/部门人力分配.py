# 3
# 3 5 3 4
max_months = int(input())
demands = [int(x) for x in input().split(" ")]
demands.sort(reverse = True)
l, r = demands[0], demands[0] + demands[1]

# 取一个最大值加一个最小值才是最优解.
# def check(hr: int, months: int, i: int):
#     if months == 0:
#         if i < len(demands):
#             return False
#         else:
#             return True
#     if i < len(demands)-1 and hr >= demands[i] + demands[i+1]:
#         return check(hr, months-1, i+2)
#     else:
#         return check(hr, months-1, i+1)

def check(hr):
    high, low = 0, len(demands)-1
    month = 0
    while high <= low:
        if demands[high] + demands[low] > hr:
            high +=1
        else:
            high +=1
            low -= 1
        month += 1
        
    if month > max_months:
        return False
    return True

while l <= r:
    hr = (l+r)//2
    if check(hr):
        r = hr-1
    else:
        l = hr+1
print(l)