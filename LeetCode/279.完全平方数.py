import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 某个整数最少的完全平方数
        dp = {}
        dp[0] = 0
        for i in range(1, n+1):
            min_num = n
            num = math.sqrt(i)//1+1
            for j in range(1, int(num)):
                min_num = min(min_num, dp[i-j*j]+1) # 这里的拆解是关键
            dp[i] = min_num
        
        return dp[n]

    ### 视作完全背包问题：n为背包容量 平方数为物品 且可以无限选
    def numSquares_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 背包
        dp = [i for i in range(n+1)] # 初始化：仅有物品1时

        max_num = math.sqrt(n)
        # 遍历物品
        for i in range(2, int(max_num)+1):
            # 遍历背包
            for j in range(i*i, n+1):
                dp[j] = min(dp[j], dp[j-i*i]+1)
        
        return dp[n]

s = Solution()
s.numSquares_1(12)





"""
广度优先搜索
数学
动态规划


"""

