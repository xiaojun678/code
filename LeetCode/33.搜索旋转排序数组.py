class Solution:
    def search(self, nums, target):
        # 二分法
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            
            # mid在上升部分
            if nums[mid]>=nums[left]:
                # 左边部分
                if nums[left]<=target<nums[mid]:
                    right = mid-1
                # 右边部分
                else:
                    left = mid+1
            # mid在下降部分
            else:
                # 右边部分
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        
        return -1


"""
数组
二分查找


"""