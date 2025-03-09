class Solution(object):
    # 深度优先遍历
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        num = 0

        def dfs(x, y):
            visited[x][y] = 1
            if grid[x][y] == '0':
                return
            # 上
            if x-1>=0 and not visited[x-1][y]:
                dfs(x-1, y)
            # 下
            if x+1<m and not visited[x+1][y]:
                dfs(x+1, y)
            # 左
            if y-1>=0 and not visited[x][y-1]:
                dfs(x, y-1)
            # 右
            if y+1<n and not visited[x][y+1]:
                dfs(x, y+1)


        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    num += 1
                    dfs(i, j)
        return num
    
    # 广度优先遍历
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        num = 0

        def bfs(x, y):
            # 队列
            queue = [(x, y)]
            visited[x][y] = 1
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while queue:
                cur_x, cur_y = queue.pop(0)

                for d in direction:
                    next_x, next_y = d
                    next_x, next_y = cur_x+next_x, cur_y+next_y

                    if next_x<0 or next_y<0 or next_x>=m or next_y>=n or grid[next_x][next_y]=='0' or visited[next_x][next_y]:
                        continue
                    else:
                        queue.append((next_x, next_y))
                        visited[next_x][next_y] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    num += 1
                    bfs(i, j)
        
        return num


"""
深度优先搜索
广度优先搜索
并查集
数组
矩阵


"""