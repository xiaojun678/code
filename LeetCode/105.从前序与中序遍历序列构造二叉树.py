# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        ### 先序
        def dfs(ino, pre):
            if not ino:
                return
            # 寻找当前节点
            # 先序第一个节点就是当前要访问的中心节点
            idx = ino.index(pre[0]) # 这里可以靠哈希表来优化-建立value-index映射
            # 建树
            root = TreeNode(pre[0])
            # 注意中序和先序的划分方法
            # 对于中序 按照中心节点分成左右两边
            # 对于先序，分别按照左边长度和右边长度往下划分
            root.left = dfs(ino[:idx], pre[1:idx+1])
            root.right = dfs(ino[idx+1:], pre[idx+1:])

            return root
        
        return dfs(inorder, preorder)


"""
树
数组
哈希表
分治
二叉树





"""



