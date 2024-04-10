#  输入</strong><br /> CA3385,CZ6678,SC6508,DU7523,HK4456,MK987<br /> 输出<br /> CA3385,CZ6678,DU7523,HK4456,MK0987,SC6508</p>
# 输入<br /> MU1087,CA9908,3U0045,FM1703<br /> 输出<br /> 3U0045,CA9908,FM1703,MU1087</strong></p> 
flights = input().split(",")
flights.sort(key = lambda x: (x[:2], int(x[2:])))
print(','.join(flights))