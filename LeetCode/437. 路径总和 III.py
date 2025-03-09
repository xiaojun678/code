from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.num = 0
        # 记录以某节点开始的路径是否已被访问过
        self.d = {}
    ### 深度优先遍历
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0

        def dfs(p, sums):
            # 经过该节点
            sums += p.val
            if sums == targetSum:
                self.num += 1
            
            if p.left:
                dfs(p.left, sums)
            if p.right:
                dfs(p.right, sums)

            # 以该节点重新开始
            if p not in self.d:
                self.d[p] = 1
                dfs(p, 0)
        
        self.d[root] = 1
        dfs(root, 0)
        return self.num

    ### 前缀和+哈希表
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        # 统计路径总次数
        ans = 0
        # 统计前缀和的出现次数
        cnt = defaultdict(int)
        cnt[0] = 1

        def dfs(node, s):
            if node is None:
                return
            nonlocal ans
            s += node.val
            ans += cnt[s - targetSum]
            cnt[s] += 1
            dfs(node.left, s)
            dfs(node.right, s)
            # 这里减1的原因是，经过节点node的路径已经访问完了，不能再保留该路径上的前缀和
            cnt[s] -= 1  # 恢复现场

        # 只遍历所有从根节点开始的路径元素和即可
        dfs(root, 0)
        return ans



"""
树
深度优先搜索
二叉树





"""



