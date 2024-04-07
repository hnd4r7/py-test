from collections import deque

# def simulate_work_queue(N, tasks, max_queue_length, num_executors):
#     queue = []  # Initialize empty work queue
#     current_time = 0  # Initialize current time
#     last_task_finish_time = 0  # Initialize last task finish time
#     discarded_tasks = 0  # Initialize count of discarded tasks

#     for i in range(N):
#         task_time = tasks[i][1]  # Get the execution time of current task

#         # Check if the work queue is full
#         if len(queue) >= max_queue_length:
#             # Check if there are idle executors at the same time as a new task submission
#             idle_executors = [exec_idx for exec_idx in range(len(queue)) if queue[exec_idx] <= current_time]

#             if not idle_executors:
#                 discarded_tasks += 1  # Increment count of discarded tasks
#                 continue

#             executor_idx = min(idle_executors)  # Choose the executor with the highest priority (lowest index)
#             queue[executor_idx] = current_time + task_time  # Update the completion time of the chosen executor's task
#         else:
#             queue.append(current_time + task_time)  # Add the completion time of the current task to the queue

#         current_time += 1  # Increment current time by 1 after each iteration

#     last_task_finish_time = max(queue)  # Find the latest completion time in the queue

#     return last_task_finish_time, discarded_tasks


# # Example usage:
# N = 3  # Number of tasks
# tasks = [(1, 3), (2, 2), (3, 3)]  # Tasks as (submission_time, execution_time) pairs
# max_queue_length = 3
# num_executors = 2

# last_task_finish_time, discarded_tasks = simulate_work_queue(N, tasks, max_queue_length, num_executors)
# print(last_task_finish_time, discarded_tasks)


task_inputs = list(map(int, input().split(" ")))
task_demands = deque()
for i in range(0, len(task_inputs), 2):
    task_demands.append((task_inputs[i], task_inputs[i+1]))
max_queue_len, max_workers = map(int, input().split(" "))
workers = [0] * max_workers  # 执行任务队列
tasks = deque()  # 未分配的任务队列
droped = 0

print("task_demands:", task_demands)
time = 0
while len(task_demands) > 0:
    t = task_demands[0]
    submit_time = t[0]
    exec_time = t[1]

    # first_idle_worker = -1
    # for i, t in enumerate(workers):
    #     if t > 0:
    #         workers[i] -= 1
    #     if workers[i] == 0 and first_idle_worker == -1:
    #         first_idle_worker = i
    # workers = list(map(lambda x: x - 1 if x > 0 else x, workers))
    workers = [x - 1 if x > 0 else x for x in workers]
    first_idle_worker = next(
        (i for i, v in enumerate(workers) if v == 0), None)

    # 同一时刻只能提交一个任务, 因此只有一个worker需要处理
    if first_idle_worker is not None and len(tasks) > 0:
        workers[first_idle_worker] = tasks.popleft()

    if time == submit_time:
        if len(tasks) >= max_queue_len:
            tasks.popleft()
            droped += 1
        tasks.append(exec_time)
        task_demands.popleft()

    if first_idle_worker is not None and len(tasks) > 0:
        workers[first_idle_worker] = tasks.popleft()

    time += 1

print("time:", time)
print("droped:", droped)
print("workers:", workers)
# print(time + task_demands[len(task_demands)-1], droped)
# print(tasks, workers)
# print(time, first_idle_worker, droped)

# submit_time exec_time
# 1 3 -> 4
# 2 2 -> 4
# 3 3 3 -> 4 + 3 = 7

# queue_len, executors
# 3 2

# _ _ _ _ _ _ _
# 1 6
# 2 4

# 3 3

# 4 3
# 6 3

# 1 2

# for i in range(len(task_demands)):
#     task_demands[i]

# exec_tasks = collections.OrderedDict(int) # submit -> start_time
# droped = 0

# for i, (submit_time, exec_time) in enumerate(task_demands):
#     # cur_time
#     time += submit_time - (exec_tasks[i-1] if i > 0 else 0)

#     #没开始
#     for td in task_demands[:min(i, max_executors)]:
#         pt_sub = td[0]
#         pt_exec = td[1]
#         if time - exec_tasks[pt_sub] > pt_exec:
#             exec_tasks.pop(pt_sub)


#     if len(exec_tasks) == queue_len:
#         # 丢弃最开始的任务
#         exec_tasks.popitem(last = False)
#         droped += 1

#     # 加入队列
#     exec_tasks[submit_time] = time

# print(time, droped)
