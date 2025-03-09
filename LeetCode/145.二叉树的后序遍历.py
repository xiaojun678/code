class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

### 递归写法
# class Solution(object):
#     def __init__(self):
#         self.res = []

#     def postorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root == None:
#             return self.res
        
#         self.postorderTraversal(root.left) # 左
#         self.postorderTraversal(root.right) # 右
#         self.res.append(root.val) # 中

#         return self.res


### 迭代写法——前序迭代的改编版
### 另一种迭代法：使用prev指针记录是否右子树已访问过 
# https://leetcode.cn/problems/binary-tree-postorder-traversal/solutions/431066/er-cha-shu-de-hou-xu-bian-li-by-leetcode-solution
class Solution(object):
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return self.res
        
        stack = [root] # 模仿前序遍历的方法
        while len(stack):
            temp = stack[-1]
            self.res.append(temp.val)
            stack.pop()

            if temp.left: 
                stack.append(temp.left)
            if temp.right: # 返回的序列是【中右左】
                stack.append(temp.right)
        
        return reversed(self.res) # 反转：【左右中】



"""
栈
树
深度优先搜索
二叉树



"""



