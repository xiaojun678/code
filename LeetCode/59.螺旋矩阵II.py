class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for _ in range(n)]

        left, right = 0, n-1
        top, bottom=  0, n-1
        k = 1
        while k<=n*n:
            # 右
            for i in range(left, right+1):
                matrix[top][i] = k
                k += 1
            top += 1
            if k>n*n:
                break
            # 下
            for i in range(top, bottom+1):
                matrix[i][right] = k
                k += 1
            right -= 1
            if k>n*n:
                break
            # 左
            for i in range(right, left-1, -1):
                matrix[bottom][i] = k
                k += 1
            bottom -= 1
            if k>n*n:
                break
            # 上
            for i in range(bottom, top-1, -1):
                matrix[i][left] = k
                k += 1
            left += 1
            if k>n*n:
                break
        
        return matrix



"""
数组
矩阵
模拟


"""