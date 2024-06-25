import collections

#  <p>2 22 1 11 4 44 5 55 3 33<br /> 1 7 2 3<br /> 输出<br /> 11 33 44 55</p> 
#  输入</strong><br /> 5 64 11 64 9 97<br /> 9 11 4 9</p>   <p>输出<br /> 97<br /> 64</p> 

msg_input = [int(x) for x in input().split(" ")]
msgs = []
for i in range(0, len(msg_input), 2):
    msgs.append([msg_input[i], msg_input[i+1]])

msgs.sort(key = lambda x: x[0])

sub_input = [int(x) for x in input().split(" ")]
subs = []
for i in range(0, len(sub_input), 2):
    subs.append([sub_input[i], sub_input[i+1]])

recvs = collections.defaultdict(list)


for msg in msgs:
    send_time = msg[0]
    msg_content = msg[1]

    send = False
    for i in range(len(subs)-1, -1, -1):
        if send:
            send = False
            break
        sub_time = subs[i][0]
        sub_cancel_time = subs[i][1]
        if send_time >= sub_time and send_time < sub_cancel_time:
            recvs[i].append(msg[1])
            send = True

consumers = list(recvs.keys())
consumers.sort()

for c in consumers:
    print(' '.join(map(lambda x: str(x), recvs[c])))