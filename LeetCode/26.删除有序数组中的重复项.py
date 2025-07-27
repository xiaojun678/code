from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ### 双指针法
        n = len(nums)
        start = 0 # 有效区间的最后一位
        for end in range(n): # 遍历数组
            if nums[start] != nums[end]:
                start += 1
                nums[start], nums[end] = nums[end], nums[start]
                
        return start + 1


"""
数组
双指针


将原问题的「最多保留 1 位」修改为「最多保留 k 位」：
1.由于是保留 k 个相同数字，对于前 k 个数字，我们可以直接保留。
2.对于后面的任意数字，能够保留的前提是：与当前写入的位置前面的第 k 个元素进行比较，不相同则保留。

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def process(nums, k):
            idx = 0
            for x in nums:
                if idx < k or nums[idx-k] != x:
                    nums[idx] = x
                    idx += 1
            return idx
        return process(nums, 1)

作者：宫水三叶
链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array/solutions/575549/shua-chuan-lc-jian-ji-shuang-zhi-zhen-ji-2eg8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""