class Solution:
    ### 动态规划 时间复杂度O(n2)
    def integerBreak(self, n: int) -> int:
        # dp[i] 正整数i的最大乘积
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(dp[j], j)*(i-j)) # 是否拆分j
        
        return dp[-1]

    ### 完全背包思想 
    # 从1～n-1中选择数字填满容量为n的背包，使其背包装满时数字乘积最大
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1

        # 物品
        for i in range(1, n):
            # 背包
            for j in range(i, n+1):
                dp[j] = max(dp[j], dp[j-i]*i)
        
        return dp[-1]



"""
数学
动态规划


"""