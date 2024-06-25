ans = 0
nums = input().split(",")
for i in range(1, len(nums)-1):
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        ans += 1
print(ans)