from typing import List, Optional


inorder_input = [int(x) for x in input().split(" ")]
preorder_input = [int(x) for x in input().split(" ")]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 报错了.
#     # 递归定义: 计算区间树节点.
#     im = { v: i for i, v in enumerate(inorder)}
#     def build(lp, rp, li, ri):
#         if lp == rp:
#             return None
#         root_val = preorder[lp]
#         left_size = im[root_val]-li
#         left_tree = build(lp+1, lp+left_size, li, li+left_size)
#         right_tree = build(lp+left_size+1, rp, li+1+left_size, ri)
#         return TreeNode(root_val, left_tree, right_tree)
#     return build(0, len(preorder)-1, 0,len(inorder)-1)

    if not preorder:
        return None
    root_val = preorder[0]
    length = inorder.index(root_val)
    left_tree = buildTree(preorder[1:length+1], inorder[:length])
    right_tree = buildTree(preorder[length+1:], inorder[length+1:])
    return TreeNode(root_val, left_tree, right_tree)

# def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#     index = {x: i for i, x in enumerate(inorder)}

#     def dfs(pre_l: int, pre_r: int, in_l: int, in_r: int) -> Optional[TreeNode]:
#         if pre_l == pre_r:  # 空节点
#             return None
#         left_size = index[preorder[pre_l]] - in_l  # 左子树的大小
#         left = dfs(pre_l + 1, pre_l + 1 + left_size, in_l, in_l + left_size)
#         right = dfs(pre_l + 1 + left_size, pre_r, in_l + 1 + left_size, in_r)
#         return TreeNode(preorder[pre_l], left, right)

#     return dfs(0, len(preorder), 0, len(inorder))  # 左闭右开区间

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/2646359/tu-jie-cong-on2-dao-onpythonjavacgojsrus-aob8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

pre_tree = buildTree(preorder_input, inorder_input)

def sum_tree(root: TreeNode):
    if root is None:
        return 0
    return root.val + (sum_tree(root.left) if root.left is not None else 0) + (sum_tree(root.right) if root.right is not None else 0)

# def change_tree(root: TreeNode):
#     root.val = sum_tree(root)
#     if root.left is not None:
#         root.left.val = sum_tree(root.left)
#     if root.right is not None:
#         root.right.val = sum_tree(root.right)

# change_tree(pre_tree)

def create_sum_tree(root):
    if root is None:
        return None
    left = create_sum_tree(root.left)
    right = create_sum_tree(root.right)
    val = sum_tree(root)-root.val
    # print(root.val, val, left, right)
    return TreeNode(val, left, right)

def print_inorder(root: TreeNode):
    if root is None:
        return
    if root.left:
        print_inorder(root.left)
    print(root.val)
    if root.right:
        print_inorder(root.right)

print_inorder(create_sum_tree(pre_tree))