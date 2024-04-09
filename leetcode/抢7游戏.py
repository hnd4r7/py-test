m = int(input())
ans = 0
def dfs(cnt, m):
    if m == 7:
        if cnt % 2 == 1:
            global ans
            ans += 1
        return
    elif m < 7:
        return
    dfs(cnt+1, m-1)
    dfs(cnt+1, m-2)
dfs(0, m)
print(ans)