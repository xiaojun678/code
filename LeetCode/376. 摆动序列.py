class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        
        res = 1 # 默认最右侧有一个峰值
        preDiff = 0
        curDiff = 0
        for i in range(len(nums)-1):
            curDiff = nums[i+1] - nums[i]
            # 判断局部峰值
            # 等于0是为了解决局部峰值存在平坡的情况
            if (preDiff <= 0 and curDiff >0) or (preDiff >= 0 and curDiff < 0): 
                res += 1
                preDiff = curDiff # 只在坡度变化的时候更新prediff 避免单调坡度有平坡的情况
        
        return res
        
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