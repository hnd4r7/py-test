from bisect import bisect_left


nums = [int(x) for x in input().split(" ")]
n = int(input())

nums.sort(reverse=True) # 任务从大到小排列. 小任务放到最后来排序
# minimal = sum(x) // n

# workers = [0]*n

# 6 2 7 7 9 3 2 1 3 11 4
# 2
def dfs(idx, threhold, workers): # 任务下标. dfs递归: idx下标的任务分配给一个worker. 
    if idx >= len(nums):
        return True
    can_assign = False
    for i in range(len(workers)):
        if workers[i] + nums[idx] > threhold:
            continue
        can_assign = True
        workers[i] += nums[idx]
        if dfs(idx+1, threhold,workers):
            return True
        workers[i] -= nums[idx]
    if not can_assign:
        return False

# min(nums) -> sum(nums)
# sum(nums)//n, 
l, r = min(nums), sum(nums)
while l <= r:
    threhold = (l+r)//2
    if dfs(0, threhold,[0]*n):
        r = threhold-1
    else:
        l = threhold+1
print(l)