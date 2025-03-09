class Solution:
    ### 两次二分查找
    def searchRange(self, nums, target):
        res = [-1, -1]
        if not nums:
            return res

        # 第一次 找左边界
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2

            # left 大于等于target的位置
            if nums[mid]<target:
                left = mid + 1
            # right 小于target的位置
            else:
                right = mid - 1
        # 是否存在target
        if left >= len(nums) or nums[left]!=target:
            return res
        
        res[0] = right + 1
        
        # 第二次 找右边界
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            # left 大于target的位置
            if nums[mid]<=target:
                left = mid + 1
            # right 小于等于target的位置
            else:
                right = mid - 1
        res[1] = left - 1

        return res  




"""
数组
二分查找

"""