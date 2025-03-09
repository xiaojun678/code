class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*n for _ in range(m)] # 到达某个位置的路径数

        for i in range(m): # 初始化
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # 本题可以进行空间优化：https://leetcode.cn/problems/unique-paths/solutions/5772/dong-tai-gui-hua-by-powcai-2
        # d[i][j]只和本行和上一行的状态有关=>两个列表
        # 进一步优化：用一个列表替换上面两个列表，即滚动更新
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

s = Solution()
print(s.uniquePaths(3, 7))


"""
数学
动态规划
组合数学


空间复杂度O(1)做法：
从左上角到右下角的过程中，我们需要移动 m+n−2 次，其中有 m−1 次向下移动，n−1 次向右移动。
因此路径的总数，就等于从 m+n−2 次移动中选择 m−1 次向下移动的方案数，即组合数



"""











