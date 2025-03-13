class Solution(object):
    ### 贪心解法 时间复杂度O(n)
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        res = 1 # 默认最右侧有一个峰值
        preDiff = 0 # nums[i] - nums[i-1]
        curDiff = 0 # nums[i+1] - nums[i]
        for i in range(len(nums)-1):
            curDiff = nums[i+1] - nums[i]
            # 判断局部峰值
            # 等于0是为了解决局部峰值存在平坡的情况
            if (preDiff <= 0 and curDiff >0) or (preDiff >= 0 and curDiff < 0): 
                res += 1
                preDiff = curDiff # 只在坡度变化的时候更新prediff 避免单调坡度有平坡的情况
        
        return res
    
    ### 动态规划 时间复杂度O(n) 空间复杂度可以进一步优化
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        # 选择一个元素作为摆动序列的一部分时，这个元素要么是上升的，要么是下降的，这取决于前一个元素的大小
        up = [1] + [0] * (n - 1) # 以前 i 个元素中的某一个为结尾的最长的「上升摆动序列」的长度
        down = [1] + [0] * (n - 1) # 以前 i 个元素中的某一个为结尾的最长的「下降摆动序列」的长度
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = max(up[i - 1] + 1, down[i - 1])
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        
        return max(up[n - 1], down[n - 1])

    ### 动态规划 时间复杂度O(n2)
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i][0] 第i个数作为山谷的最长子序列
        # dp[i][1] 第i个数作为山峰的最长子序列
        dp = [[1, 1] for _ in range(len(nums))] # 初始化

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] < nums[j]: # 山谷
                    dp[i][0] = max(dp[i][0], dp[j][1]+1) # 前一个数作为山峰
                if nums[i] > nums[j]:  # 山峰
                    dp[i][1] = max(dp[i][1], dp[j][0]+1) # 前一个数作为山谷
        
        return max(dp[-1][0], dp[-1][1])


        
        
s = Solution()
print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))





"""
贪心
数组
动态规划

解题关键：
https://code-thinking-1253855093.file.myqcloud.com/pics/20201124174327597.png

局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值。
整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列。

实际操作上，只需要统计数组的峰值数量就可以了（相当于是删除单一坡度上的节点，然后统计长度）

这就是贪心所贪的地方，让峰值尽可能的保持峰值，然后删除单一坡度上的节点

还存在三种特殊情况需要考虑：https://www.programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html

本题也可以使用动态规划求解
"""