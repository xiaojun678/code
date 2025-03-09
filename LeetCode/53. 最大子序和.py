class Solution(object):
    ### 暴力求解法：超出时间限制
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     maxSum = -10e4

    #     for i in range(len(nums)):
    #         count = 0
    #         for j in range(i, len(nums)):
    #             count += nums[j]
    #             if count > maxSum:
    #                 maxSum = count

    #     return maxSum


    ### 贪心法
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     maxSum = -10e4
    #     count = 0
    #     for i in range(0, len(nums)):
    #         count += nums[i]
    #         if count > maxSum:
    #             maxSum = count
    #         if count < 0: # 当某个序列之和为负值时就丢弃
    #             count = 0

    #     return maxSum

    ### 动态规划
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 下标前i个字符的最大和
        dp = [0]*len(nums) # 还可以进一步优化空间
        dp[0] = nums[0] 

        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        
        return max(dp)




s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



"""
数组
分治
动态规划


贪心算法：
局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”
因为负数加上下一个元素 “连续和”只会越来越小。

全局最优：选取最大“连续和”

问：为什么不能从连续和的中间位置重新开始？
答：对于某个保留的连续和，其任意前n个子序列之和一定大于等于0
现在需要放弃该连续和序列，即该连续和序列的值为负
如果从中间开始，那么就要再减去一段正值=>变得更负


本题也可以使用动态规划、分治法求解


也可以使用前缀和求解：
https://leetcode.cn/problems/maximum-subarray/solutions/2533977/qian-zhui-he-zuo-fa-ben-zhi-shi-mai-mai-abu71


"""