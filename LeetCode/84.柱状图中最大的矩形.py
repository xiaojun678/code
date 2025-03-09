class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # https://blog.csdn.net/Zolewit/article/details/88863970
        ans = 0
        # 存放下标 从底至顶递增
        stack = []
        # 在前面加上0是为了出栈后栈为空的情况，这样就计算不了stack[-1] 如[2,1]算例
        # 在后面加上0是为了保证最后所有元素都能出栈 因为当前元素在出栈时才会计算以其高度的最大面积
        heights = [0] + heights + [0]
        
        for i in range(len(heights)):
            # 确保递增
            while len(stack) and heights[i]<heights[stack[-1]]:
                tmp = stack.pop()
                # 以heights[tmp]为高的面积：右边界i  左边界stack[-1] 最后还要减一
                ans = max(ans, heights[tmp]*(i-stack[-1]-1))
            stack.append(i)

        return ans


s = Solution()
s.largestRectangleArea([1,3,3,1])

"""
栈
数组
单调栈

"""

