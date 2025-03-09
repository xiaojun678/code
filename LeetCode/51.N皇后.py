class Solution:
    ### 灵神做法
    # 每行一定只能放一个皇后：所以按行递增，每次循环列即可
    # 冲突判断：只和过去已经确定的皇后比较
    # O(1)判断是否和已有皇后冲突：
    # 判断列是否有冲突 行无需判断——每行递增
    # 对于斜方向：↗方向的格子，行号加列号是不变的；↖方向的格子，行号减列号是不变的。
    def solveNQueens(self, n):
        res = []
        queens = [0] * n  # 皇后放在 (r,queens[r]) 下标表示行号 元素表示列号

        col = [False] * n # 标记之前放置的皇后的列号
        diag1 = [False] * (n * 2 - 1) # 标记之前放置的皇后的行号加列号
        diag2 = [False] * (n * 2 - 1) # 标记之前放置的皇后的行号减列号
        def dfs(r):
            if r == n:
                res.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens])
                return
            # 在 (r,c) 放皇后
            for c, ok in enumerate(col):
                # 判断能否放皇后：列、↗和↖
                if not ok and not diag1[r + c] and not diag2[r - c]:  
                    queens[r] = c  # 后续可以直接覆盖，无需再恢复现场
                    col[c] = diag1[r + c] = diag2[r - c] = True  # 皇后占用了 c 列和两条斜线
                    dfs(r + 1) # 行号递增
                    col[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场
        dfs(0)
        return res

    
    ### 简单做法
    def solveNQueens(self, n):
        result = []  # 存储最终结果的二维字符串数组

        chessboard = ['.' * n for _ in range(n)]  # 初始化棋盘
        self.backtracking(n, 0, chessboard, result)  # 回溯求解
        return [[''.join(row) for row in solution] for solution in result]  # 返回结果集

    def backtracking(self, n, row, chessboard, result):
        if row == n:
            result.append(chessboard[:])  # 棋盘填满，将当前解加入结果集
            return

        # 只循环列 行每次加一
        for col in range(n):
            if self.isValid(row, col, chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]  # 放置皇后
                self.backtracking(n, row + 1, chessboard, result)  # 递归到下一行
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]  # 回溯，撤销当前位置的皇后


    # 不需要检查行 因为在回溯中一行只会放一个
    # 且只检查上方的皇后，下方区域无需考虑
    def isValid(self, row, col, chessboard):
        # 检查列
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False  # 当前列已经存在皇后，不合法

        # 检查 45 度角是否有皇后
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False  # 左上方向已经存在皇后，不合法
            i -= 1
            j -= 1

        # 检查 135 度角是否有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False  # 右上方向已经存在皇后，不合法
            i -= 1
            j += 1

        return True  # 当前位置合法

    ### 复杂做法
    def solveNQueens(self, n):
        res = []
        path = []
        visited = [[0]*n for _ in range(n)]

        # n皇后可以攻击到的位置
        def n_pos(x, y, value):
            # 同一列
            for i in range(n):
                visited[i][y] -= value
            # 同一行
            for j in range(n):
                visited[x][j] -= value
            # 左斜线
            x_, y_ = x, y
            while x>0 and y>0:
                x-=1
                y-=1
            while x<n and y<n:
                visited[x][y] -= value
                x+=1
                y+=1
            # 右斜线
            x, y = x_, y_
            while x<n-1 and y>0:
                x+=1
                y-=1
            while x>=0 and y<n:
                visited[x][y] -= value
                x-=1
                y+=1

        def digui(x):
            if len(path) == n:
                res.append(path[:])
                return

            if x>=n: # 确保不走回头路
                return

            for i in range(x, n):
                for j in range(n):
                    if visited[i][j]>=0:
                        path.append((i,j))
                        n_pos(i,j,1)

                        digui(i+1)

                        path.pop()
                        n_pos(i,j,-1)

        digui(0)
        
        result = []
        for r in range(len(res)):
            tmp1 = []
            for i in range(n):
                tmp2 = ''
                for j in range(n):
                    if (i, j) in res[r]:
                        tmp2+='Q'
                    else:
                        tmp2+='.'
                tmp1.append(tmp2)
            result.append(tmp1)
        return result

s = Solution()
print(s.solveNQueens(4))


"""
数组
回溯



"""