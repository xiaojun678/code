class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []

        def digui(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                digui(i+1, path) # 从下一个数开始
                path.pop()
        digui(0, path)
        return res


s = Solution()
s.subsets([1,2])



"""
位运算
数组
回溯


"""