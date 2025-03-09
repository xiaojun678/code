class Solution(object):
    # https://www.programmercarl.com/0031.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%8E%92%E5%88%97.html
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 从后向前遍历 找到第一个逆序对（小-大）
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    # 交换这个逆序对
                    nums[i], nums[j] = nums[j],nums[i]

                    # 并对后面部分进行反转，使其变为从小到大排序
                    left, right = i+1, len(nums)-1
                    while left <= right:
                        nums[left], nums[right] = nums[right], nums[left]
                        left += 1
                        right -= 1
                    return
        # 一个逆序对也找不到 说明数组是从大到小排列的
        # 此时完全反转即可
        nums.reverse()



"""
数组
双指针

"""

