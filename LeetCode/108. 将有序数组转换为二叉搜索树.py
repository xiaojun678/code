# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    ### 递归法
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def digui(lis):
            if not lis:
                return None

            mid = len(lis)//2
            root = TreeNode(lis[mid])
            root.left = digui(lis[:mid])
            root.right = digui(lis[mid+1:])

            return root
        
        return digui(nums)
    ### 迭代法
    """
    初始化，先对数据进行一次二分，找出左子树(数组)，根节点，右子树(数组)，使其进入栈。
    不断处理栈内根节点，并使其与左右子树的根节点相连接，实际是进行深度遍历构造树的连接。
    https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/solutions/
    """
    def splitBinaryTree(self, nums):
        mid = len(nums) // 2
        if (len(nums) - 1) == mid:
            right = []
            left = nums[:mid]
        else:
            right = nums[mid + 1:]
            left = nums[:mid]
        return [left, TreeNode(nums[mid]), right]
    
    def sortedArrayToBST(self, nums):
        if len(nums) == 1:
            return TreeNode(nums[0])
        res = []
        left_nums, root, right_nums = self.splitBinaryTree(nums)
        stack = [[left_nums, root, right_nums]]
        while stack:
            left, mid_node, right = stack.pop()
            if left:
                l_left, l_mid_node, l_right = self.splitBinaryTree(left)
                mid_node.left = l_mid_node
                stack.append([l_left, l_mid_node, l_right])
                if not right:
                    res.extend([mid_node.val])
            if right:
                r_left, r_mid_node, r_right = self.splitBinaryTree(right)
                mid_node.right = r_mid_node
                stack.append([r_left, r_mid_node, r_right])
                if not left:
                    res.extend([None, mid_node.val])
        return root






"""
树
二叉搜索树
数组
分治
二叉树



"""

