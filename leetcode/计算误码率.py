s1 = input()
s2 = input()

# 2A4B  3A3B
# 2A 2B
ans = 0
while len(s1) >= 2 and len(s2) >= 2:
    ca, cb = int(s1[0]), int(s2[0])
    a, b = s1[1], s2[1]

    if ca == cb:
        if a != b:
            ans += ca
        s1 = s1[2:]
        s2 = s2[2:]
    else:
        if ca > cb:
            s1 = str(ca-cb)+s1[1:]
            s2 = s2[2:]
        else:
            s2 = str(cb-ca)+s2[1:]
            s1 = s1[2:]
        if a != b:
            ans += min(ca,cb)
    
    print(s1, s2)
ans += len(s1) if s1 else len(s2)

print(ans)