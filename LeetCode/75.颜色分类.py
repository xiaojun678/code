class Solution:
    ### 两次遍历
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 先移0
        left = 0
        for right in range(len(nums)):
            if nums[right]==0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        # 再移1
        for right in range(len(nums)):
            if nums[right]==1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

    ### 一次遍历
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # first表示第一个大于0所在的位置
        # second表示第一个大于1所在的位置
        first, second = 0, 0
        for third in range(len(nums)):
            if nums[third] == 1:
                nums[second], nums[third] = nums[third], nums[second]
                second += 1
            if nums[third] == 0:
                nums[first], nums[third] = nums[third], nums[first]
                if first < second: # 已经将一些 1 连续地放在头部，此时一定会把一个 1 交换出去，导致答案错误
                    nums[second], nums[third] = nums[third], nums[second]

                first += 1
                second += 1


"""
数组
双指针
排序


"""