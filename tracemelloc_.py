import tracemalloc

tracemalloc.start()

x = [1 for _ in range(10000000)]
y = x[1:]
# ... run your application ...
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)