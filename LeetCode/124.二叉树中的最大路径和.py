# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_path = -float('inf')
    ### 深度优先遍历 与543题类似
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(r):
            if not r:
                return 0
            left = dfs(r.left)
            right = dfs(r.right)

            path = r.val + left + right
            self.max_path = max(path, self.max_path)

            return max(0, r.val+left, r.val+right)
        dfs(root)
        return self.max_path





"""
树
深度优先搜索
动态规划
二叉树



"""



