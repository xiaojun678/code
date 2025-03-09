# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### 迭代法
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res
        
        queue = [root] # 使用队列
        num1 = 1 # 记录当前层的节点数
        while num1: # 当前层没有节点时结束循环
            r = []
            num2 = 0 # 记录下一层的节点数
            while num1: # 某一层的结点全部出队列 同时下一层的元素进队列
                temp = queue.pop(0)
                r.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                    num2 += 1
                if temp.right:
                    queue.append(temp.right)
                    num2 += 1
                num1 -= 1
            num1 = num2
            res.append(r)
        
        return res

            
        


"""
树
广度优先搜索
二叉树

递归解法：记住当前节点的层数
class Solution(object):
	def levelOrder(self, root):
		if not root:
			return []
		res = []
		def dfs(index,r):
			# 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
			if len(res)<index:
				res.append([])
			#  将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
			# res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
			res[index-1].append(r.val)
			# 递归的处理左子树，右子树，同时将层数index+1
			if r.left:
				dfs(index+1,r.left)
			if r.right:
				dfs(index+1,r.right)
		dfs(1,root)
		return res

作者：王尼玛
链接：https://leetcode.cn/problems/binary-tree-level-order-traversal/solutions/85075/die-dai-di-gui-duo-tu-yan-shi-102er-cha-shu-de-cen/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



"""
