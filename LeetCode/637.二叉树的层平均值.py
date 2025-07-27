from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 层序遍历
        res = []

        queue = [root]

        while queue:
            sums = 0
            count = 0
            size = len(queue)
            for _ in range(size):
                p = queue.pop(0)

                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)

                sums += p.val
                count += 1
            
            res.append(sums/count)
        
        return res




"""
树
深度优先搜索
广度优先搜索
二叉树


层序遍历属于广度优先搜索
深度优先遍历亦可：记录当前深度的加和与计数，所有的遍历完成后再依次计算平均值即可

"""