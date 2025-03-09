class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1) # 保证查询效率
        nums2 = list(set(nums2)) # 去重
        res = []
        for i, _ in enumerate(nums2):
            if nums2[i] in nums1:
                res.append(nums2[i])
        return res

s = Solution()
print(s.intersection([1,2,2,1], [2,2]))

"""
数组
哈希表
双指针
二分查找
排序



存放结果可以直接用set，以避免重复值
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)
"""

