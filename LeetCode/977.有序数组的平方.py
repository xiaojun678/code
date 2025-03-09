class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        res = []
        while left<=right:
            if nums[left]*nums[left] > nums[right]*nums[right]:
                res.append(nums[left]*nums[left])
                left += 1
            else:
                res.append(nums[right]*nums[right])
                right -= 1
        res.reverse()
        return res



"""
数组
双指针
排序

"""