class Solution(object):
    ### 贪心算法 & 动态规划
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        # 前i+1个数据的最小值
        # 可以优化成O(1)：记住最小的值即可
        dp = [prices[0]]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i]-dp[i-1])
            
            dp.append(min(prices[i], dp[i-1]))
        return profit






"""
数组
动态规划


"""