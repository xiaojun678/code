class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        ### 空间复杂度O(n)
        # # 前缀乘积
        # mp1 = [1]*(len(nums)+1)
        # for i in range(len(nums)):
        #     mp1[i+1] = mp1[i]*nums[i]
        # # 后缀乘积
        # mp2 = [1]*(len(nums)+1)
        # for i in range(len(nums)-1,-1,-1):
        #     mp2[i] = mp2[i+1]*nums[i]
        
        # for i in range(len(nums)):
        #     ans.append(mp1[i]*(mp2[i+1]))

        ### 空间复杂度O(1)
        prev = 1
        # 前向遍历
        for i in range(len(nums)):
            if i == 0:
                ans.append(1)
            else:
                prev *= nums[i-1]
                ans.append(prev)
        # 后向遍历
        prev = 1
        for i in range(len(nums)-2, -1, -1):
            prev *= nums[i+1]
            ans[i] *= prev
        
        return ans

        ### 双指针同时遍历可以更快


s = Solution()
print(s.productExceptSelf([1,2,3,4]))


"""
数组
前缀和



"""