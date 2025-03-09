class Solution(object):
    ### 动态规划
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 包含前i个数的最长递增子序列
        dp = [1]*len(nums)
        max_num = 0
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            max_num = max(max_num, dp[i])
        
        return max_num

    ### 动态规划+贪心+二分查找
    # https://leetcode.cn/problems/longest-increasing-subsequence/solutions/7196/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，
        则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小
        """
        size = len(nums)
        # 特判
        if size < 2:
            return size

        # tail[i]：长度为 i + 1 的 所有 上升子序列的结尾的最小值
        # 可证明tail数组一定是严格递增的
        # 数组 tail 不是问题中的「最长上升子序列」，只是用于求解 LIS 问题的状态数组
        tail = [nums[0]]

        for i in range(1, size):
            """
            逻辑：
            1.在遍历数组 nums 的过程中，看到一个新数 num，如果这个数 严格 大于有序数组 tail 的最后一个元素，
            就把 num 放在有序数组 tail 的后面，否则进入第 2 点；
            
            2.在有序数组 tail 中查找第 1 个等于大于 num 的那个数，试图让它变小；
            2.1 
            如果有序数组 tail 中存在 等于 num 的元素，什么都不做，因为以 num 结尾的最短的「上升子序列」已经存在；
            2.2 
            如果有序数组 tail 中存在 大于 num 的元素，找到第 1 个，让它变小，这样就找到了一个结尾更小的相同长度的上升子序列。
            """
            # 先尝试是否可以接在末尾
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue

            # 使用二分查找法，在有序数组 tail 中找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小
            left = 0
            right = len(tail) - 1
            while left <= right:
                # 选左中位数不是偶然，而是有原因的，原因请见 LeetCode 第 35 题题解
                # mid = left + (right - left) // 2
                mid = (left + right) >> 1
                if tail[mid] < nums[i]:
                    # 中位数肯定不是要找的数，把它写在分支的前面
                    left = mid + 1
                else:
                    right = mid - 1
            # 第一个大于等于nums[i]的元素
            tail[left] = nums[i]
        
        return len(tail)









"""
数组
二分查找
动态规划



"""

