m = {}
for i in range(1, 10):
    m[chr(i)] = chr(ord('a') + i)

for i in range(10, 27):
    m[str(i) + "*"] = chr(ord('j') + i-10)

s = input()
ans = ""
i = 0
while i < len(s):
    if s[i+2] == "*":
        ans += str(m[s[i:i+3]])
        i+=3
    else:
        print(s[i])
        ans += str(m[s[i]])
        i+=1
print(ans)
