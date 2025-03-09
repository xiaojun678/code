class Solution(object):
    ### Z字法 时间复杂度O(m+n)
    def searchMatrix(self, matrix, target):
        row, col = 0, len(matrix[0])-1

        while 0<=row<len(matrix) and 0<=col<len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return False


    ### 二分查找 时间复杂度O(logmn)
    def searchMatrix(self, matrix, target):
        # 把矩阵每一行拼在一起，可以得到一个递增数组
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1

        while left<=right:
            mid = (left+right)//2

            if matrix[mid//n][mid%n] < target: # 不需要真的拼接
                left = mid + 1
            else:
                right = mid - 1
        # left是大于等于target的下标
        return matrix[left//n][left%n] == target if left<m*n else False


s = Solution()
s.searchMatrix([[1]], 2)



"""
数组
二分查找
矩阵


"""