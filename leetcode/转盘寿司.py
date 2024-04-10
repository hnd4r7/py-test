susi = [int(x) for x in input().split(" ")]
n = len(susi)
susi += susi
st = [] # 递增栈
nxt = [-1] * len(susi)

# 3 15 6 14 3 15 6 14
for i, v in enumerate(susi):
    while st and v < susi[st[-1]]:
        nxt[st[-1]] = i
        st.pop()
    st.append(i)

for i, x in enumerate(nxt):
    # if nxt[i] != -1:
    #     if nxt[i-n] == -1:
    #         exit(1)
    #     nxt[i-n] = nxt[i]

    if x >= n:
        nxt[i] = x-n

ans = [0] * n
for i in range(0, n):
    ans[i] = susi[i] + susi[nxt[i]] if nxt[i] != -1 else susi[i]

print(ans)


