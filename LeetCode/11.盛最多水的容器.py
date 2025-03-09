class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 初始化左指针和右指针
        left = 0
        right = len(height)-1
        # 初始化最大面积为0
        maxArea = 0
        # 当左指针小于右指针时，继续循环
        while left<right:
            # 计算当前面积
            area = (right-left)*(height[left] if height[left]<height[right] else height[right])
            # 更新最大面积
            maxArea = maxArea if maxArea>area else area
            # 小的需要移动
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        # 返回最大面积
        return maxArea

"""
贪心
数组
双指针



"""


