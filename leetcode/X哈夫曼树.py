# https://renjie.blog.csdn.net/article/details/135609956
n = input()
nodes = [x for x in input().split(" ")]
nodes.sort()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

presum = [0] * n
sum_tmp = 0
for i, n in enumerate(nodes):
    sum_tmp += n
    presum[i] = sum_tmp

# for i in range(n-1, -1, 1):
def build(i, root):
    if i == 1:
        root.left = TreeNode(nodes[0])
        root.right = TreeNode(nodes[1])
    elif nodes[i] < presum[i-1]:
        root.left = TreeNode(nodes[i])
        root.right = build(i-1, TreeNode())
    else:
        root.left = build(i-1, TreeNode())
        root.right = TreeNode(nodes[i])
    return root

t = build(n-1, TreeNode())

# sum to tree


# print in order



