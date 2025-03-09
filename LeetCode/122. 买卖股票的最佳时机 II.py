class Solution(object):
    ### 贪心算法：把所有的涨幅都赚到 把所有的跌幅都躲过 就是最大利润
    # 把利润分解为每天为单位的维度，而不是从 0 天到第 3 天整体去考虑！
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i]-prices[i-1]>0:
                profit += prices[i]-prices[i-1]
        
        return profit

    ### 动态规划
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][0] 第 i 天交易完后手里没有股票的最大利润
        # dp[i][1] 第 i 天交易完后手里持有一支股票的最大利润
        dp = [(0, -prices[0])]

        for i in range(1, len(prices)):
            ## 每天的行为就两种：购买（减去价格）或卖出（加上价格）
            # 第i天手里没有股票：第i-1天原本就没有 或 第i-1天有但是卖出
            tmp1 = max(dp[i-1][0], dp[i-1][1]+prices[i]) # 直接加价格 成本之前已考虑
            # 第i天手里有股票：第i-1天原本就有 或 第i-1天没有但是买入
            tmp2 = max(dp[i-1][1], dp[i-1][0]-prices[i])

            dp.append((tmp1, tmp2))
        
        return max(dp[-1][0], dp[-1][1])


"""
贪心
数组
动态规划

"""




