class Solution(object):
    ### 暴力求解法
    # def rotate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     for _ in range(k):
    #         num = nums[-1]
    #         for j in range(len(nums)-1, 0, -1):
    #             nums[j] = nums[j-1]
    #         nums[0] = num
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ### 空间复杂度为O(n)
        # 规律：下标为i移动k后所在的位置:(i+k)%len(nums)
        # n = len(nums)
        # temp = nums[:]
        # for i, num in enumerate(temp):
        #     nums[(i+k)%n] = num
        
        ### 空间复杂度为O(1)
        n = len(nums)
        k = k%n # 简化k

        # 翻转列表
        def reverse(i, j):
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        
        # 整体翻转
        reverse(0, n-1)
        # 翻转左边
        reverse(0, k-1)
        # 翻转右边
        reverse(k, n-1)

        print(nums)



s = Solution()
s.rotate([-1,-100,3,99],2)


"""
数组
数学
双指针



"""

            