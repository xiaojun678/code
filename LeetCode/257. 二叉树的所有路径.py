# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        res = []
        path = []

        def digui(p):

            path.append(p.val)

            if not p.left and not p.right: # 叶子节点
                res.append(path[:])
            else: # 非叶子节点
                if p.left:
                    digui(p.left)
                if p.right:
                    digui(p.right)
            
            path.pop() # 回溯
        
        digui(root)

        # 转换格式
        tmp = []
        for r in res:
            t = ''
            for i in range(len(r)):
                t += str(r[i])

                if i != len(r) - 1:
                    t += '->'
            tmp.append(t)
        return tmp


"""
树
深度优先搜索
字符串
回溯
二叉树

"""