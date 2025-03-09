class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                if n1 + nums[j] == target:
                    return [i, j]
        return None

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n1 in enumerate(nums):
            if target - n1 in d:
                return [d[target-n1], i]
            d[n1] = i
        return []



s = Solution1()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))


"""
数组
哈希表

改进方法：

注意到方法一的时间复杂度较高的原因是寻找 target - x 的时间复杂度过高。
因此，我们需要一种更优秀的方法，能够快速寻找数组中是否存在目标元素。如果存在，我们需要找出它的索引。

使用哈希表，可以将寻找 target - x 的时间复杂度降低到从 O(N) 降低到 O(1)。

对于每一个x，在查询x时将x的值与下标存到字典里
这样对于后面的x，再直接查询时即可判断字典里是否存在target-x的值即可

空间复杂度：O(N)

作者：力扣官方题解
链接：https://leetcode.cn/problems/two-sum/solutions/434597/liang-shu-zhi-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


"""