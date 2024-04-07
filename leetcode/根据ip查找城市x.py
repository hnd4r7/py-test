import collections

import ipaddress

def check_in_range(ip_min, ip_max, ip):
    ip_min = ipaddress.ip_address(ip_min)
    ip_max = ipaddress.ip_address(ip_max)
    target_ip = ipaddress.ip_address(ip)
    
    return ip_min <= target_ip <= ip_max

ip_min = '192.168.0.1'
ip_max = '192.168.0.255'
ip = '192.168.0.100'

result = check_in_range(ip_min, ip_max, ip)


ip_ranges = input().split(";")
range_dict = collections.defaultdict(list)
for r in ip_ranges:
    city, ipr = r.split('=')
    iprs = ipr.split(',')
    range_dict[city].append(iprs)

req_ips = input().split(',')
for r in req_ips:
    min_range = ''