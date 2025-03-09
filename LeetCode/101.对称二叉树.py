from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    ### 递归法
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return not root or recur(root.left, root.right)

    ### 迭代法：层序遍历
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root.left and not root.right:
            return True
        elif not root.left:
            return False
        elif not root.right:
            return False
        
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)

        while queue:
            size = len(queue)
            for _ in range(0, size, 2): # 一次弹出两个
                left = queue.popleft()
                right = queue.popleft()

                if left.val != right.val:
                    return False
                
                if left.left and right.right:
                    queue.append(left.left)
                    queue.append(right.right)
                elif not left.left and right.right:
                    return False
                elif not right.right and left.left:
                    return False
                
                if left.right and right.left:
                    queue.append(left.right)
                    queue.append(right.left)
                elif not left.right and right.left:
                    return False
                elif not right.left and left.right:
                    return False

        return True


"""
树
深度优先搜索
广度优先搜索
二叉树



"""