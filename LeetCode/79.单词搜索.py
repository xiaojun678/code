class Solution:
    def exist(self, board, word):
        flag = False
        visited = set()
        strs = ''
        def digui(start_x, start_y):
            # 不满足条件的情况
            nonlocal strs
            nonlocal flag
            if flag or start_x>=len(board) or start_x<0 or start_y>=len(board[0]) or start_y<0 or board[start_x][start_y]!=word[len(strs)] or (start_x, start_y) in visited:
                return
            
            strs += word[len(strs)]
            visited.add((start_x, start_y))

            if len(strs) == len(word):
                flag = True
                return

            # 上下左右四个方向
            digui(start_x+1, start_y)
            digui(start_x-1, start_y)
            digui(start_x, start_y+1)
            digui(start_x, start_y-1)

            # 回溯
            strs = strs[:-1]
            visited.remove((start_x, start_y))


        for i in range(len(board)):
            for j in range(len(board[0])):
                if not flag:
                    digui(i, j)
        return flag

"""
数组
字符串
回溯
矩阵


短暂更改board[i][j]以达到不重复访问的目的
https://leetcode.cn/problems/word-search/solutions/2361646/79-dan-ci-sou-suo-hui-su-qing-xi-tu-jie-5yui2
"""