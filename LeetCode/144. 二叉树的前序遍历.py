# 定义二叉树节点
class TreeNode(object):
    def __init__(self, val=0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

### 递归写法
# class Solution(object):
#     def __init__(self):
#         self.res = []

#     def preorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root == None:
#             return self.res
        
#         self.res.append(root.val) # 中
#         self.preorderTraversal(root.left) # 左
#         self.preorderTraversal(root.right) # 右

#         return self.res

### 迭代写法
class Solution(object):
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return self.res
        
        stack = []
        stack.append(root)

        while len(stack):
            temp = stack[-1] # 先出栈
            self.res.append(temp.val)
            stack.pop()

            if temp.right: # 再依次把右孩子和左孩子加入栈
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        
        return self.res



# s = Solution()
# a = [1,None,2,3]

"""
栈
树
深度优先搜索
二叉树



"""
        
        