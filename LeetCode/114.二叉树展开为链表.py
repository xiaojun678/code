from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.pre = None

    ### 头插法：访问顺序：右左中
    # 相当于是先序遍历的逆序版
    # 最先访问的是最后一个节点 依次让当前节点指向上一个访问的节点
    def flatten(self, root):
        if root is None:
            return
        self.flatten(root.right) # 右
        self.flatten(root.left) # 左
        # 中
        root.left = None
        root.right = self.pre  # 头插法，连接上一个节点
        self.pre = root
    
    ### 一般递归
    def flatten(self, root):
        """
        递归的一个非常重要的点就是：
        不去管函数的内部细节是如何处理的，我们只看其函数作用以及输入与输出
        
        1.函数作用：将一个二叉树，原地将它展开为链表
        2.输入：树的根节点
        3.输出：无

        https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/218689/114-er-cha-shu-zhan-kai-wei-lian-biao-by-ming-zhi-
        """
        if root is None:
            return
        ## 把左子树变成链表
        self.flatten(root.left)
        ## 把右子树变成链表 
        self.flatten(root.right)

        ## 合并当前节点的左子树和右子树
        # 暂时记录右子树
        tmp = root.right
        # 把树的右边换成左边的链表
        root.right = root.left
        # 树的左边置空
        root.left = None

        # 找到树的最右边的节点
        while root.right:
            root = root.right
        # 把右边的链表接到刚才树的最右边的节点
        root.right = tmp


    ### 先先序遍历 再手动展开链表 空间复杂度为O(N)
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        # 先序遍历
        stack = deque()
        res = []
        stack.append(root)
        while stack:
            p = stack.pop()
            res.append(p)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        for i in range(1, len(res)):
            res[i-1].left = None
            res[i-1].right = res[i]
        res[-1].right = None
        res[-1].left = None

        return res[0]


"""
栈
树
深度优先搜索
链表
二叉树

空间复杂度为O(1)的见官解https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/356853/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu
"""


