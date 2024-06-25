import collections


matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix = [[1,2,3], [4,5,6], [7,1,4]] # => 3 传送之后 4-1
m, n = len(matrix), len(matrix[0])
dp = [[0] * n for _ in range(m)] 
dp[0][0] = 0

teleport = collections.defaultdict(list)

for i in range(m):
    for j in range(n):
        teleport[matrix[i][j]].append((i,j))
        # dp[i][j] = 
        pass