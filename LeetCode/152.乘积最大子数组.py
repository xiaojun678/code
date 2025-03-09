class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] 包含第i个字符最大值和最小值
        dp = [(nums[0], nums[0])]
        max_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i]>=0:
                ma = max(dp[i-1][0]*nums[i], nums[i]) # 舍弃
                mi = min(dp[i-1][1]*nums[i], nums[i])
            else:
                ma = max(dp[i-1][1]*nums[i], nums[i])
                mi = min(dp[i-1][0]*nums[i], nums[i])
            dp.append((ma,mi))
            max_num = max(max_num, dp[-1][0])
        
        return max_num




"""
数组
动态规划




"""



