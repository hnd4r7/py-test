heap_size = 100
req = int(input())
q = []
while True:
    line = input()
    if line:
        start, length = line.split(" ") 
        q.append((int(start), int(length)))
    else:
        break

for i in range(0, len(q)-1):
    possible_start = q[i][0] + q[i][1]
    if q[i+1][0] - possible_start > req:
        print(possible_start)
else:
    print(-1)
