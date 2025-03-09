# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    ### 递归法
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root: 
            return 
        tmp = root.left # 暂存左子树
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root

    
    ### 迭代法：先序遍历
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root: 
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: 
                stack.append(node.left)
            if node.right: 
                stack.append(node.right)

            node.left, node.right = node.right, node.left
        return root

    ### 统一迭代法：先序遍历
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        stack = [root]

        while stack:
            p = stack.pop()
            if p!=None:
                # 前序 中序 后序均可
                if p.right:
                    stack.append(p.right)
                if p.left:
                    stack.append(p.left)
                stack.append(p)
                stack.append(None)

            if p == None:
                p = stack.pop()
                # 交换        
                p.right, p.left = p.left, p.right
        
        return root


s = Solution()

r1 = TreeNode(4)
r2 = TreeNode(2)
r3 = TreeNode(1)
r4 = TreeNode(3)
r5 = TreeNode(7)
r1.left = r2
r2.left = r3
r2.right = r4
r1.right = r5

print(s.invertTree(r1))
            


"""
树
深度优先搜索
广度优先搜索
二叉树


"""