import collections
import functools

class FileInfo:
    def __init__(self, access_count, access_time, size):
        self.access_count = access_count
        self.access_time = access_time
        self.size = size 

max_cache_size = int(input())
op_count = int(input())
ops = [input().split(" ") for _ in range(op_count)]

total_size = 0
cache = collections.defaultdict(FileInfo) # file name: (count of access, last_access_time)
time = 0

def cmp(x, y):
    if cache[x].access_count != cache[y].access_count:
        return cache[x].access_count - cache[y].access_count
    return cache[x].access_time - cache[y].access_time

for op in ops:
    time += 1
    operation, file_name, *args  = op
    if operation == 'get':
        cache[file_name].access_count += 1
        cache[file_name].access_time = time
    elif operation == 'put':
        if file_name in cache:
            continue
        size = int(args[0])
        if total_size + size > max_cache_size:
            ks = list(cache.keys())
            ks.sort(key = functools.cmp_to_key(cmp), reverse = False)
            for i in range(len(ks)):
                total_size -= cache[ks[i]].size 
                cache.pop(ks[i])
                if total_size + size <= max_cache_size:
                    break
        cache[file_name] = FileInfo(0, time, size)
        total_size += size
    else:
        break

ks = list(cache.keys())
ks.sort(key = functools.cmp_to_key(lambda x, y: x < y), reverse = False)
print(ks)

"""
50
6
put a 10
put b 20
get a
get a
get b
put c 30
"""