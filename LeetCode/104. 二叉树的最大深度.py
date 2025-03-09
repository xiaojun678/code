from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.max_depth = 0
    ### 递归法：先序遍历
    ### 后序遍历更简单：不需要max_depth记录
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def digui(p, depth):
            if not p:
                return
            else:
                depth += 1
                self.max_depth = max(self.max_depth, depth)

            digui(p.left, depth)
            digui(p.right, depth)
        
        digui(root, 0)
        return self.max_depth

    ### 迭代法：层序遍历
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            size = len(queue)
            depth += 1
            for _ in range(size):
                p = queue.popleft()

                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
        
        return depth




"""
树
深度优先搜索：先序 中序 后序
广度优先搜索：层序
二叉树

"""


