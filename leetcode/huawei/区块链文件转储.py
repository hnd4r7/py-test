# 100 300 500 400 400 150 100
nums = [int(x) for x in input().split(" ")]
l, r, total = 0, 0, 0
ans = 0
while r < len(nums):
    if total + nums[r] <= 1000:
        total += nums[r]
        ans = max(ans, total)
        r += 1
    else:
        total -= nums[l]
        l += 1
print(ans)