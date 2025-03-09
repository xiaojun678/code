class Solution(object):
    ### 模拟法 空间复杂度O(m*n)
    ### 可以进一步优化空间———访问过的元素直接设置为None
    # def spiralOrder(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     m, n = len(matrix), len(matrix[0])
    #     tmp = [[1 for _ in range(n)] for _ in range(m)]

    #     i = j = 0
    #     ans  = []
    #     while len(ans)<m*n:
    #         # 分别对应四个方向
    #         while j<n and tmp[i][j]:
    #             ans.append(matrix[i][j])
    #             tmp[i][j]=0
    #             j+=1
    #         j-=1
    #         i+=1

    #         while i<m and tmp[i][j]:
    #             ans.append(matrix[i][j])
    #             tmp[i][j]=0
    #             i+=1
    #         i-=1   
    #         j-=1

    #         while j>=0 and tmp[i][j]:
    #             ans.append(matrix[i][j])
    #             tmp[i][j]=0
    #             j-=1
    #         j+=1
    #         i-=1

    #         while i>=0 and tmp[i][j]:
    #             ans.append(matrix[i][j])
    #             tmp[i][j]=0
    #             i-=1
    #         i+=1                
    #         j+=1
    #     return ans   
    
    ### 通过设置上下左右四个边界来控制
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])

        left = 0
        right = n-1
        top = 0
        bottom = m-1

        ans  = []
        while 1:
            # 从左到右
            for j in range(left, right+1):
                ans.append(matrix[top][j])
            top += 1
            if top>bottom: # 需要及时判断是否已经打印完
                break
            
            # 从上到下
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            if right<left: # 需要及时判断是否已经打印完
                break
            
            # 从右到左
            for j in range(right, left-1, -1):
                ans.append(matrix[bottom][j])
            bottom -= 1
            if top>bottom: # 需要及时判断是否已经打印完
                break 

            # 从下到上
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
            left += 1
            if right<left: # 需要及时判断是否已经打印完
                break
        return ans



s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

"""
数组
矩阵
模拟


"""


