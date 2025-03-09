class Solution(object):
    ### 动态规划-可以直接修改原矩阵来达到O(1)空间
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0]*len(grid[0])]*len(grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                elif i==0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j==0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]

    ### 回溯法-超出时间限制
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        min_num = float('inf')

        def digui(x, y, path):
            if x>=m or y>=n:
                return
            
            path.append(grid[x][y])

            if x==m-1 and y==n-1:
                nonlocal min_num
                min_num = min(min_num, sum(path))
            
            digui(x+1,y,path[:])
            digui(x,y+1,path[:])

        digui(0, 0, [])

        return min_num
    
"""
数组
动态规划
矩阵


"""