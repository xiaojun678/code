# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ### 本题是求高度，需要后序遍历-从底至上
    def isBalanced(self, root):
        flag = True
        def digui(p):
            if not p:
                return 0
        
            leftDepth = digui(p.left) # 访问左节点
            rightDepth = digui(p.right) # 访问右节点

            if abs(leftDepth - rightDepth) > 1: # 访问当前节点
                nonlocal flag
                flag = False
            
            return max(leftDepth, rightDepth) + 1

        digui(root)
        return flag

"""
树
深度优先搜索
二叉树


求深度适合用前序遍历，而求高度适合用后序遍历
"""