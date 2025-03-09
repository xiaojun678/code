class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 本题也可以进行空间上的优化
        dp = [float('inf')]*(len(cost)+1) # 爬到第i个台阶需要的最小花费
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])

        return dp[-1]
    

s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))


"""
数组
动态规划


"""