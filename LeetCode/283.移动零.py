# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         end = len(nums) - 1

#         for i in range(end-1,-1,-1): # 倒着移动
#             if nums[i] == 0:
#                 for j in range(i+1, len(nums)):
#                     nums[j-1] = nums[j]
#                 nums[end] = 0


class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        left = right = 0  # 左指针始终指向0 右指针向右移动 不为0时和左指针的数交换
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1



s = Solution()
s.moveZeroes([1])




"""
数组
双指针

方法：双指针

使用双指针，左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。

右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移。

注意到以下性质：

左指针左边均为非零数；

右指针左边直到左指针处均为零。

因此每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变。


"""