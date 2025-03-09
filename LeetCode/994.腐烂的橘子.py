class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # 获取所有新鲜和腐烂橘子
        new = set()
        old = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    new.add((i, j))
                if grid[i][j] == 2:
                    old.add((i, j))
        
        # 时间流逝
        time = 0
        while new:
            flag = 0
            tmp = []
            for i,j in old:
                # 只腐烂新鲜的橘子
                # 上 
                if i-1>=0 and (i-1, j) in new:
                    new.remove((i-1, j))
                    tmp.append((i-1, j))
                    flag = 1
                # 下
                if i+1<m and (i+1, j) in new:
                    new.remove((i+1, j))
                    tmp.append((i+1, j))
                    flag = 1
                # 左
                if j-1>=0 and (i, j-1) in new:
                    new.remove((i, j-1))
                    tmp.append((i, j-1))
                    flag = 1
                # 右
                if j+1<n and (i, j+1) in new:
                    new.remove((i, j+1))
                    tmp.append((i, j+1))
                    flag = 1
            # 一轮结束后再更新腐烂的橘子 避免当轮被腐烂的在当轮就进行扩散
            for i, j in tmp:
                old.add((i, j))
            
            # 一轮下来没有任何变化时即永远不可能再继续腐烂
            if flag == 0:
                return -1
            
            time += 1
        
        return time


"""
广度优先搜索
数组
矩阵


"""