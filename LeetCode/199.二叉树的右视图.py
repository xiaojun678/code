from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    ### 迭代法：层序遍历
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                p = queue.popleft()
                temp.append(p.val)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            res.append(temp[-1])
        
        return res

    ### 递归法：先访问右子树 再访问左子树 当某个深度首次到达时，对应的节点就在右视图中
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        def dfs(r, depth):
            if not r:
                return
            # 该深度第一次到达
            if depth == len(res):
                res.append(r.val)
            
            # 访问右子树
            dfs(r.right, depth+1)
            # 访问左子树
            dfs(r.left, depth+1)

        dfs(root, 0)
        return res





"""
树
深度优先搜索
广度优先搜索
二叉树



"""


