class Solution(object):
    ### 完全背包问题：物品为硬币且无限 背包为总金额
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        # 物品
        for i in range(len(coins)):
            # 背包
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]]+1)
        
        return dp[amount] if dp[amount]!=float('inf') else -1


    ### 常规动态规划
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 下标为i表示i所需最少的银币数
        dp = [0]

        for i in range(1, amount+1):
            min_num = amount
            for c in coins:
                if i-c >=0:
                    min_num = min(min_num, dp[i-c])
            dp.append(min_num + 1)
        
        return dp[amount] if dp[amount]<=amount else -1


"""
广度优先搜索
数组
动态规划

"""
