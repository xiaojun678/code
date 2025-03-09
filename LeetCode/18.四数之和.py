class Solution(object):
    ### 双指针-与三数之和思路相同
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []

        for first in range(n):
            # 保证四元组不重复
            if first != 0 and nums[first] == nums[first-1]:
                continue
            for second in range(first+1, n):
                if second != first+1 and nums[second] == nums[second-1]:
                    continue
                
                tmp = target - nums[first] - nums[second]
                # 双指针
                fourth = n - 1
                for third in range(second+1, n):
                    if third != second+1 and nums[third] == nums[third-1]:
                        continue
                    # 右指针向左滑动
                    while third < fourth and nums[third] + nums[fourth] > tmp:
                        fourth -= 1
                    
                    if third >= fourth:
                        break

                    if nums[third] + nums[fourth] == tmp:
                        res.append([nums[first], nums[second], nums[third], nums[fourth]])

        return res
    


"""
数组
双指针
排序

"""

