from collections import defaultdict


class Solution(object):
    ### 暴力解法——超时
    # def subarraySum(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     num = 0
    #     left = right = 0

    #     while left < n:
    #         temp = 0
    #         while right < n:
    #             temp += nums[right]
    #             if temp == k:
    #                 num += 1
    #             right += 1
    #         left += 1
    #         right = left
    #     return num
    
    
    ### 前缀和+哈希表优化
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mp = [0]*(len(nums)+1)
        # 计算前缀和
        # 定义mp[i]为下标0到i-1个数字之和
        for i in range(len(nums)):
            mp[i+1] = nums[i]+mp[i]
        
        d = defaultdict(int)
        num = 0
        # 下标i到j-1元素之和
        # sum(i,j) = sum(j)-sum(i)=k ==> sum(j) = sum(i)+k  其中i<j
        # i表示过去的数 j表示未来的数
        for j in range(0, len(nums)+1):
            num += d[mp[j]] # 使用过去存储的数
            d[mp[j]+k] += 1 # 存储下来方便后续使用

        return num

s = Solution()
print(s.subarraySum([1], 1))

"""
数组
哈希表
前缀和


https://leetcode.cn/problems/subarray-sum-equals-k/solutions/2781031/qian-zhui-he-ha-xi-biao-cong-liang-ci-bi-4mwr

"""




