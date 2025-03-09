class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 排序
        nums = sorted(nums)
        res = []

        # 从小到大确定第一个数
        for first in range(len(nums)-2):
            # 确保第一个数不大于0
            if nums[first]>0:
                break

            # 要确保相邻两个数不能重复
            if first > 0 and nums[first] == nums[first-1]:
                continue 

            target = -nums[first]
            # 第三个数的指针
            third = len(nums)-1
            # 从小到大确定第二个数
            for second in range(first+1, len(nums)-1):
                # 要确保相邻两个数不能重复
                if second > first+1 and nums[second] == nums[second-1]:
                    continue

                # 随着第二个数逐渐变大 第三个数就随之逐渐变小
                # 不断向左移动第三个数的指针
                while nums[second]+nums[third] > target and third > second:
                    third -= 1
                
                # 第二个数和第三个数相遇时退出循环
                if third == second:
                    break

                if nums[second]+nums[third] == target:
                    res.append([nums[first], nums[second], nums[third]])
        
        return res


s = Solution()
print(s.threeSum([-1,-1,0,1,2,4]))


"""
数组
双指针
排序


当我们需要枚举数组中的两个元素时，如果我们发现随着第一个元素的递增，第二个元素是递减的，
那么就可以使用双指针的方法，将枚举的时间复杂度从 O(N2) 减少至 O(N)


"""





