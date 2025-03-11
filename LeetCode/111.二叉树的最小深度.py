from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ### 自顶向下递
    def minDepth(self, root):
        depth = float('inf')

        def digui(p, num):
            nonlocal depth
            if not p:
                return
            
            num += 1
            if not p.left and not p.right:
                depth = min(depth, num)
                return
            
            digui(p.left, num)
            digui(p.right, num)
        
        digui(root, 0)
        return 0 if depth == float('inf') else depth

    ### 层序遍历
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        
        return 0







"""
树
深度优先搜索
广度优先搜索
二叉树


"""