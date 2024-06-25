from typing import Optional


nums = [int(x) for x in input().split(" ")]

class Node:
    def __init__(self, val, left=None, right=None, mid=None):
        self.val = val
        self.left = left
        self.right = right
        self.mid = mid

root = Node(nums[0])

def insert_tri(root, v):
    if root.val == v:
        if root.mid is None:
            root.mid = Node(v)
        else:
            insert_tri(root.mid, v)
    elif root.val > v:
        if root.right is None:
            root.right = Node(v)
        else:
            insert_tri(root.right, v)
    elif root.val < v:
        if root.left is None:
            root.left = Node(v)
        else:
            insert_tri(root.left, v)

def max_depth(root):
    if root is None:
        return 0
    return 1+max(max_depth(root.left), max_depth(root.right), max_depth(root.mid))

for x in nums[1:]:
    insert_tri(root, x)

print(max_depth(root))