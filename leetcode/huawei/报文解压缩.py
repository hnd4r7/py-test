payload = "3[m2[u]]"
# 递归
"""
def dicipher(i) -> tuple[int, str]:
    cnt = 0
    content = ''
    while i < len(payload):
        if payload[i].isdigit():
            digit_start = i
            while payload[i].isdigit():
                i+=1
            cnt = int(payload[digit_start:i])
        elif payload[i] == "[":
            i+=1
            content_start = i
            while payload[i] > 'a' and  payload[i] < 'z':
                i+=1
            content = payload[content_start:i]
            if payload[i].isdigit():
                i, nxt_content = dicipher(i)
                content += nxt_content
        elif payload[i] ==']':
            i+=1
            break
    return i, content * cnt

i = 0
content = ''
while i < len(payload):
    i, pre = dicipher(i)
    content += pre

print(content)
"""
# stack
s = []
content = ''
for c in payload:
    s.append(c)
    if c == "]":
        s.pop()
        #逆序解开
        tc = ''
        while s and s[-1] > 'a' and  s[-1] < 'z':
            tc = s.pop() + tc
        if s[-1] == "[":
            s.pop()
        cnt = ''
        while s and s[-1].isdigit():
            cnt = s.pop() + cnt
        cnt = int(cnt)
        s.append(tc * cnt) # 计算出来的结果重新入栈 !!!
print(s[0])


