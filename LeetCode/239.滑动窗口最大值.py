from collections import deque

class Solution(object):
    ### 暴力解法——超时
    # def maxSlidingWindow(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     n = len(nums)
    #     ans = [max(nums[:k])]
    #     for i in range(1, n-k+1):
    #         if nums[i-1] == ans[i-1]:
    #             ans.append(max(nums[i:i+k]))
    #         else:
    #             ans.append(max(nums[i+k-1], ans[i-1]))
    #     return ans

    ### 单调递减双端队列（可以快速的在队列头部和尾部添加、删除元素）
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque()
        ans = []
        for i in range(len(nums)):
            # 元素进队列
            # 当队列中的元素小于新进来的元素时就全部出栈（一定不会为后续的最大值）
            while len(d)>0 and nums[d[-1]]<=nums[i]:
                d.pop()
            d.append(i)
            # 元素出队列
            # 判断队首最大元素是否已经被滑动窗口滑过
            if i-d[0]>=k:
                d.popleft()
            # 统计最大值
            if i>=k-1:
                ans.append(nums[d[0]])
        return ans


s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))



"""
队列
数组
滑动窗口
单调队列
堆（优先队列）



双端队列：
可以在队首和队尾进行插入和删除操作。在两端插入和删除元素的时间复杂度为 O(1)，
而在中间插入或删除的时间复杂度为 O(n)。

单调队列套路
1.入（元素进入队尾，同时维护队列单调性）
2.出（元素离开队首）
3.记录/维护答案（根据队首）


此题也可以使用优先队列（堆）-heapq 来实现 调整滑动窗口内的最大值仅需O(logn)时间复杂度

"""

