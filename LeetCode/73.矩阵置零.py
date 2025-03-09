class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ### 空间复杂度O(m+n)
        # # 记录行
        # row = set()
        # # 记录列
        # column = set()

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==0:
        #             row.add(i)
        #             column.add(j)
        # # 行置为0
        # while len(row):
        #     t = row.pop()
        #     for j in range(len(matrix[0])):
        #         matrix[t][j] = 0
        # # 列置为0
        # while len(column):
        #     t = column.pop()
        #     for i in range(len(matrix)):
        #         matrix[i][t] = 0

        ### 空间复杂度为O(1) 但会损害一定时间复杂度
        for i in range(len(matrix)):
            # 记录当前行是否已经要为0
            cur_row = -1
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    cur_row = i
                    break
            if cur_row>=0:
                for j in range(len(matrix[0])):
                    if matrix[i][j]:
                        matrix[cur_row][j] = 2e31 # 标记一下

        for j in range(len(matrix[0])):
            # 记录当前列是否已经要为0
            cur_column = -1
            for i in range(len(matrix)):
                if matrix[i][j]==0:
                    cur_column = j
                    break
            if cur_column>=0:
                for i in range(len(matrix)):
                    if matrix[i][j]:
                        matrix[i][cur_column] = 2e31

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==2e31:
                    matrix[i][j]=0

        print(matrix)


s = Solution()
s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])


"""
数组
哈希表
矩阵


空间复杂度为O(1)的其他方法：

我们可以用矩阵的第一行和第一列代替空间复杂度为O(m+n)中的两个标记数组，以达到 O(1) 的额外空间。
但这样会导致原数组的第一行和第一列被修改，无法记录它们是否原本包含 0。
因此我们需要额外使用两个标记变量分别记录第一行和第一列是否原本包含 0。

在实际代码中，我们首先预处理出两个标记变量，接着使用其他行与列去处理第一行与第一列，
然后反过来使用第一行与第一列去更新其他行与列，最后使用两个标记变量更新第一行与第一列即可。

"""

