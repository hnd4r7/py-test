board = []
target = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
for _ in range(9):
    row = input().split(" ")
    board += [[int(val) if val != '0' else 0 for val in row]]

def check(x, y):
    # 检查已经填入的坐标是否和列中有的元素相等
    for i in range(9):
        if i != x and board[i][y] == board[x][y]:
            return False
    # 检查已经填入的坐标是否和行中有的元素相等
    for j in range(9):
        if j != y and board[x][j] == board[x][y]:
            return False
 
    # 检查每个正方形是否符合（粗线框内只有1~9）
    m, n = 3*(x // 3), 3*(y // 3)  # 这里求出的是3x3网格的左上角的坐标
    for i in range(3):
        for j in range(3):
            if(i+m != x or j+n != y) and board[i+m][j+n] == board[x][y]:
                return False 
    return True

def dfs():
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                for x in range(1, 10):
                    board[i][j] = x
                    if check(i, j) and dfs():
                        return True
                    board[i][j] = 0
                return False
    return True
dfs()

for row in board:
    print(' '.join(map(str, row)))
