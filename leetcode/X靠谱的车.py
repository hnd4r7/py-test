x = int(input())

p = 0 # 当前位数
k = 0
while x > 0:
    last_digit = x % 10
    if last_digit > 4:
        skiped += p
    skiped += 
    x = x // 10
    p *= 10

print(skiped)
