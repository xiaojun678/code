class Solution(object):
    ### 滑动时间窗口
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        left_index, right_index = 0, 10e5
        ans = 0
        while right<len(nums):
            ans += nums[right]

            while ans >= target:
                if right-left+1<right_index-left_index+1:
                    right_index, left_index = right, left

                ans -= nums[left]
                left += 1
            
            right += 1
        
        return right_index-left_index+1 if right_index-left_index!=10e5 else 0
    
s = Solution()
print(s.minSubArrayLen(4, [1,4,4]))