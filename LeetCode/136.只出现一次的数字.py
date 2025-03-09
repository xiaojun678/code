class Solution:
    def singleNumber(self, nums):
        # 异或：两个相同数字异或为0  与0异或等于自身
        res = nums[0]

        for i in range(1, len(nums)):
            res ^= nums[i]
        
        return res


"""
位运算
数组

"""