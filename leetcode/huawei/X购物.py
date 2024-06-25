from queue import PriorityQueue


nums = [1,1,2,3,3]
K = 6
# 至少一件商品不同.
"""
[0]
[1]
[0] + [1]
[2]
[0] + [2]
[1] + [2]
[3]
[0] + [3]
[1] + [3]
[2] + [3]
[4]
[0] + [4]
"""


# 对 nums 数组进行排序
nums.sort()

# 定义一个以元素为 Integer[] 类型的优先队列 queue
queue = PriorityQueue(lambda a, b: a[0] + nums[a[1]] - (b[0] + nums[b[1]]))
c = [0, 0] # sum, idx

output_str = ""

i = 1
while True:
    if i > K:
        # 当 i 大于 m 时输出 output_str 并结束循环
        print(output_str)
        break
    else:
        # 否则将 c[0] + nums[c[1]] 加入 output_str
        output_str += str(c[0] + nums[c[1]]) + "\n"
        if c[1] + 1 >= len(nums):
            # 如果 c[1] 加 1 大于等于 n，则取出队列中的元素赋值给 c
            c = queue.poll()
        else:
            # 否则将 c[0] + nums[c[1]] 和 c[1] + 1 加入队列，同时更新 c 值
            queue.put([c[0] + nums[c[1]], c[1] + 1])
            c[1] += 1
            queue.put(c)
            c = queue.poll()

    i += 1

