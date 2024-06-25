directions = [[-1,-1]]


m = 40
n = 40
k = 18

i = j = ans = 0

# def dfs(i, j):
#     if 
#     return 1 + dfs(i-1)

def sum_digit(i):
    ans = 0
    while i > 0:
        ans += i % 10
        i //= 10
    return ans

while i < m:
    if sum_digit(i) + sum_digit(j) <= k:
        ans += 1
    # ans += 1
    if j == n-1:
        i+=1
        j=0
    else:
        j+=1
print(ans)

