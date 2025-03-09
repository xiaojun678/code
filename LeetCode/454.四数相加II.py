from collections import defaultdict

class Solution(object):
    # 哈希表保存两两数组之和
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        n = len(nums1)
        # 保存前两个数组之和
        sums1 = defaultdict(int) # 默认为0
        # 保存后两个数组之和
        sums2 = defaultdict(int)
        for first in range(n):
            for second in range(n):
                sums1[nums1[first]+nums2[second]] += 1
        for third in range(n):
            for forth in range(n):
                sums2[nums3[third]+nums4[forth]] += 1
        
        # 统计次数
        res = 0
        for key, val in sums1.items():
            if -key in sums2:
                res += sums1[key] * sums2[-key]
        
        return res


"""
数组
哈希表

本题可以直接使用一个sums，即在计算后两个数组之和时直接使用sums1来相加次数

"""



















