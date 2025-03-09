class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ### 空间复杂度为O(n)
        # nums = set(nums)
        # idx = 1
        # while 1:
        #     if idx not in nums:
        #         return idx
        #     idx += 1

        # # 靠修改原数组的值来实现空间复杂度为O(1)
        # # 对于长度为n的数组 要么缺失的值在1-n之间 要么是n+1
        # # 先把负数和0替换掉 方便后面的标记 确保所有数都是正数
        # n = len(nums)
        # for i in range(n):
        #     if nums[i]<=0:
        #         nums[i] = n+1 # 大于n的数就可以
        # # 此时，若某个数是小于等于n的 就代表这个数出现
        # # 把下标为这个数-1位置的数标记
        # # 即：靠下标来标记某个数是否存在
        # for i in range(n):
        #     # 取绝对值的目的是因为它可能已经被打了标记
        #     num = abs(nums[i])
        #     if num <= n:
        #         nums[num-1] = -abs(nums[num-1])
        # # 如果某个下标对应的元素不是负数 那么这个下标+1对应的值就不存在
        # for i in range(n):
        #     if nums[i]>0:
        #         return i+1
        
        # return n+1

        ### 还可以使用交换的方法
        # 即：若nums[i]在1-n之间 就把nums[i]和nums[nums[i]-1]的数进行交换
        # 全部交换完成后 某个下标x位置的值不等于x+1时 即为缺少的第一个数
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1


s = Solution()
print(s.firstMissingPositive([3,4,-1,1]))


"""
数组
哈希表


如果题目给定的数组是不可修改的，那么就不存在满足时空复杂度要求的算法；
但如果我们可以修改给定的数组，那么是存在满足要求的算法的。



"""