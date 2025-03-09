class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n]*m
        # 和第62题一样 空间也可以进行优化
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1: # 有障碍 保持为0 不进行计算
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


s = Solution()
print(s.uniquePathsWithObstacles([[0,1],[0,0]]))


"""
数组
动态规划
矩阵


"""
