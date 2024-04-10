# https://renjie.blog.csdn.net/article/details/128158438

dna = input()
win = int(input())

cnt = len([x for x in dna[:win] if x in ["C", "G"]])
max_cnt = cnt
start_pos = 0

for i in range(win, len(dna)):
    if dna[i] in ["C", "G"]:
        cnt += 1
    if dna[i-win] in ["C", "G"]: # i-win 已经出队伍
        cnt -= 1
    print(f"index: {i} {dna[i-win+1:i+1]}->{cnt}") # 区间: [i-win+1, cnt)
    if cnt > max_cnt:
        max_cnt = max(max_cnt, cnt)
        start_pos = i-win+1
print(dna[start_pos:start_pos+win])


