class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = right = 0 # left指向特定值, right向右探索
        k = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                k += 1
        return k

s = Solution()
print(s.removeElement([3,2,2,3], 3))

"""
快指针和慢指针：
快指针：向右探索
慢指针：指向特定值，当快指针不等于特定值时进行交换


数组
双指针
"""
