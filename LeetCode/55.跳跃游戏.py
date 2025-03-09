class Solution(object):
    ### 贪心算法 && 动态规划
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 前i个能最远到达的下标
        dp = [nums[0]]

        for i in range(1, len(nums)):
            if dp[i-1]<i:
                dp.append(0)
            else:
                dp.append(max(dp[i-1], i+nums[i]))
        return dp[-1]>=(len(nums)-1)
    
    ### 简化版
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_path = 0
        for i in range(len(nums)):
            if max_path>=i:
                max_path = max(max_path, i+nums[i])
            else:
                return False
        
        return max_path>=(len(nums)-1)





"""
贪心
数组
动态规划


"""
