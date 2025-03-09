# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    ### 递归法
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # 节点i允许的最小值和最大值
        def digui(r, mi, ma):
            # 从顶至下：先序
            if not r:
                return True
            if mi!=None and r.val<=mi:
                return False
            if ma!=None and r.val>=ma:
                return False

            flag1 = True if not r.left else digui(r.left, mi, min(r.val, ma) if ma!=None else r.val)
            flag2 = True if not r.right else digui(r.right, max(r.val, mi) if mi!=None else r.val, ma)
            return flag1 and flag2
        return digui(root, None, None)

    ### 迭代法
    def isValidBST(self, root):
        # 中序遍历
        stack = []
        p = root
        pre = -float('inf') # 记录前一个值
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                if p.val<=pre:
                    return False
                
                pre = p.val
                p = p.right
        return True


"""
树
深度优先搜索
二叉搜索树
二叉树


二叉搜索树的中序遍历一定是有序的（反之也成立），所以可以使用迭代法进行中序遍历来判断
"""