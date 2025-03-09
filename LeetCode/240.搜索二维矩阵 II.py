class Solution(object):
    ### 二分查找 逐行查找
    # 时间复杂度为O(mlogn)
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     m, n =len(matrix), len(matrix[0])
    #     start = 0
    #     end = m-1

    #     for i in range(m):
    #         if matrix[i][-1]<target:
    #             start+=1
    #     for j in range(m-1,-1,-1):
    #         if matrix[j][0]>target:
    #             end-=1
    #     def binarySearch(l, t):
    #         left = 0
    #         right = len(l)-1
    #         # 定义区间[left, right]
    #         while left<=right:
    #             mid = (left+right)/2
    #             if l[mid]>t:
    #                 right = mid-1
    #             elif l[mid]<t:
    #                 left = mid+1
    #             else:
    #                 return True
    #         return False

    #     for i in range(start, end+1):
    #         if binarySearch(matrix[i], target):
    #             return True
    #     return False
    
    ### 从右上角往左下角看是一棵二叉搜索树
    # 时间复杂度O(m+n)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n =len(matrix), len(matrix[0])
        i = 0
        j = n-1
        while i<m and j>=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        
        return False


"""
数组
二分查找
分治
矩阵



"""