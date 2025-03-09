class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = (left + right)//2
            if nums[m] > target:
                right = m - 1
            elif nums[m] < target:
                left = m + 1
            else:
                return m
        return -1


s = Solution()
print(s.search([-1,0,5],-1))


"""
数组
二分查找



二分查找

重点是理解区间的含义：
1.将区间定义为[left, right]
>target:right = m-1
<target:left = m+1

2.将区间定义为[left, right)
>target:right = m
<target:left = m+1


=========扩展=========

1. left为第一个大于等于target的   right为第一个小于target的
while left<=right:
    mid = (left+right)//2

    if nums[mid]<target: # 没有等号
        left = mid + 1
    else:
        right = mid -1


2. left为第一个大于target的   right为第一个小于等于target的
while left<=right:
    mid = (left+right)//2

    if nums[mid]<=target: # 有等号
        left = mid + 1
    else:
        right = mid -1  

"""
