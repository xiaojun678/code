class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

### 递归写法
# class Solution(object):
#     def __init__(self):
#         self.res = []

#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root == None:
#             return self.res
        
#         self.inorderTraversal(root.left) # 左
#         self.res.append(root.val) # 中
#         self.inorderTraversal(root.right) # 右

#         return self.res

class Solution(object):
    def __init__(self):
        self.res = []
    ### 迭代写法
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return self.res

        stack = []
        p = root
        
        while len(stack) or p:
            if p!=None: # 一直向左访问
                stack.append(p)
                p = p.left
            else: # 出栈并且向右访问
                self.res.append(stack[-1].val)
                p = stack[-1].right

                stack.pop()
        return self.res
    
    ### 颜色标记法：前、中、后序遍历的代码可以保持一致
    """
    使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
    如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
    如果遇到的节点为灰色，则将节点的值输出。
    https://leetcode.cn/problems/binary-tree-inorder-traversal/solutions/25220/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right)) # 先加右节点
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


"""
栈
树
深度优先搜索
二叉树


"""