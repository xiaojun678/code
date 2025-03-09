# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.path = []
    
    ### 先分别求到达两节点的路径 再取最近公共祖先
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 求到达某节点的路径
        res = []

        def dfs(root, path, target):
            if not root:
                return
            if root == target:
                path.append(root)
                res.append(path[:])
                return
            # 回溯法
            path.append(root)
            dfs(root.left, path, target)
            dfs(root.right, path, target)
            path.pop()
        
        dfs(root, [], p)
        dfs(root, [], q)

        res1, res2 = res[0],res[1]
        for r1 in res1[::-1]:
            if r1 in res2:
                return r1
            
    ### 深度优先遍历
    def lowestCommonAncestor(self, root, p, q):
        """
        一定存在LCA的话，分两种情况：
        1.在当前节点时，往下找发现p q分别在当前节点的左右子树各一个，
        那么不用考虑了，LCA一定是当前节点，因为p,q分别在当前节点的左右子树中。
        2.p q都在当前节点的一侧，在某一侧递归找p,q，先找到了谁就直接返回谁就行，
        因为他们在一侧，没被找到的那个一定在找到的那个p/q的下边，那么无疑LCA就是先找到的这个p/q
        """
        if root in (None, p, q): # 先找到哪一个就返回哪一个
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # 左右都找到
            return root  # 当前节点是最近公共祖先
        return left or right # 找到哪一个就返回哪一个 都没找到就返回None



"""
树
深度优先搜索
二叉树



"""