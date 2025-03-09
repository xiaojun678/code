from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.val = None
    ### 迭代方式
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # 中序遍历
        stack = deque()
        p = root
        res = []
        num = 0
        while (p or stack) and num < k:
            if p:
                stack.append(p)
                p = p.left
            else:
                res.append(stack[-1].val)
                num += 1
                p = stack.pop().right
        return res[-1]

    ### 递归
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def dfs(r, num):
            if r.left:
                num = dfs(r.left, num)
            num += 1
            if num == k:
                self.val = r.val
            if r.right:
                num = dfs(r.right, num)
            return num
        
        dfs(root,0)
        return self.val

"""
树
深度优先搜索
二叉搜索树
二叉树

官方解答中有此题的进阶版：
（1）需要频繁地查找第 k 小的值，将如何优化算法？
（2）如果二叉搜索树经常被修改（插入/删除操作）并且需要频繁地查找第 k 小的值，你将如何优化算法？
https://leetcode.cn/problems/kth-smallest-element-in-a-bst/solutions/1050055/er-cha-sou-suo-shu-zhong-di-kxiao-de-yua-8o07
"""


