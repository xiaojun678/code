class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] i个节点的二叉搜索树数量
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j] # dp[i-1]+dp[i-2]*dp[1]+dp[i-3]*dp[2]...
        return dp[-1]


"""
树
二叉搜索树
数学
动态规划
二叉树

"""