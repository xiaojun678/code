class Solution(object):
    ### 动态规划
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i][0] 不偷第i个 dp[i][1] 偷第i个
        dp = [[0, nums[0]]]

        for i in range(1, len(nums)):
            # 不偷第i个
            tmp1 = max(dp[-1][0], dp[-1][1])
            # 偷第i个
            tmp2 = dp[-1][0] + nums[i]

            dp.append([tmp1, tmp2])
        
        return max(dp[-1][0], dp[-1][1])

    ### 动态规划
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        # dp[i]表示满足条件的前i个能偷的最大金额
        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            # 不偷第i个：dp[i-1]
            # 偷第i个：dp[i-2]+nums[i]
            dp.append(max(dp[i-1], dp[i-2]+nums[i]))
        
        return dp[-1]






"""
数组
动态规划

https://leetcode.cn/problems/house-robber/solutions/28242/da-jia-jie-she-dong-tai-gui-hua-jie-gou-hua-si-lu-
"""