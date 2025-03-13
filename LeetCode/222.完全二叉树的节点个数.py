# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ### 完全二叉树的解法 时间复杂度为O(log n × log n)
    def countNodes(self, root):
        if not root:
            return 0
        left = root.left
        right = root.right
        leftDepth = 0 # 这里初始为0是有目的，为了下面求指数方便
        rightDepth = 0
        while left: # 求左子树深度
            left = left.left
            leftDepth += 1
        while right: # 求右子树深度
            right = right.right
            rightDepth += 1
        if leftDepth == rightDepth: # 左右子树深度相同为满二叉树 直接使用公式计算
            return (2 << leftDepth) - 1 # 注意(2<<1) 相当于2^2，所以leftDepth初始为0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1 # 不相等则继续寻找为满二叉树的子树

    ### 普通二叉树的解法 时间复杂度为O(n)
    def countNodes(self, root):
        if not root:
            return 0
        
        queue = [root]
        num = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                p = queue.pop(0)
                num += 1
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
        
        return num


"""
位运算
树
二分查找
二叉树


"""