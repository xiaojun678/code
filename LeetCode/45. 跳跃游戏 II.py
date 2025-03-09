class Solution(object):
    ### 贪心法 & 动态规划
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 跳到前i步的最小跳跃数
        dp = [0]*len(nums)
        start = 1
        for i in range(0, len(nums)):
            end = min(len(nums), i + nums[i] + 1)
            for j in range(start, end):
                # 贪心法
                dp[j] = dp[i]+1
                
                if j == end-1:
                    start = end
        return dp[-1]
    

    ### 进一步优化
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        maxPos = 0 # 能到达最远的地方
        end = 0 # 某一段最远点
        # 只需要运行到倒数第二个数
        # i=end num继续+1 i<end 直接返回当前num
        # 如果运行到最后一个数 num可能会重复+1
        for i in range(len(nums)-1):
            maxPos = max(maxPos, i+nums[i])
            if i == end:
                num += 1
                end = maxPos
        
        return num







s = Solution()
s.jump([2,1])



"""
贪心
数组
动态规划

"""
