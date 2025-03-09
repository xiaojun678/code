from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.ans = 0
    ### 递归法
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # dfs(node) 表示从节点node开始往下的最长路径长度
        # 显然经过某一个节点node的最长路径长度为： dfs(node.left) + dfs(node.right)
        def dfs(node):
            if not node:
                return 0
            # 该节点左边最深
            l = dfs(node.left)
            # 该节点右边最深
            r = dfs(node.right)
            # 记录全局最长路径
            self.ans = max(self.ans, l+r)

            # 当前节点的最深等于左节点最深和右节点最深的最大值
            return max(l, r)+1

        dfs(root)
        return self.ans
    ### 迭代法：层序遍历
    def diameterOfBinaryTree(self, root):
        """
        https://leetcode.cn/problems/diameter-of-binary-tree/solutions/1034062/yan-du-you-xian-sou-suo-bfsjie-jue-by-hi-bqla/
        """
        maxl, q = 0, [(root)]
        nodes = deque()
        while q:
            p = q.pop(0)
            if p.left: q.append(p.left)
            if p.right: q.append(p.right)
            nodes.appendleft(p)
        
        for p in nodes:
            l = p.left.val if p.left else 0
            r = p.right.val if p.right else 0
            maxl = max(l + r, maxl)
            p.val = max(l, r) + 1 # 这里改了节点的值 表示经过该节点的最长直径
        
        return maxl









"""
树
深度优先搜索
二叉树

"""