class Solution(object):
    ### 01背包问题：背包-sums 物品-nums元素
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sums = sum(nums)
        if sums%2!=0:
            return False
        sums = int(sums/2)

        dp = [float('inf')]*(sums+1) # 多初始化一个 方便判断j-i=0的情况
        dp[0] = 0
        # 物品
        for i in nums:
            # 背包
            for j in range(sums, i-1, -1):
                dp[j] = min(dp[j], dp[j-i])
        
        return dp[sums]!=float('inf')
    
    ### 简化版
    def canPartition(self, nums):
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [0] * (target + 1)
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = max(dp[j], dp[j-num] + num)
        return dp[-1] == target




s = Solution()
s.canPartition([1,5,11,5])

"""
数组
动态规划

"""