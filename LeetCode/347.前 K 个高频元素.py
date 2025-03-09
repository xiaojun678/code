from collections import defaultdict
import heapq

class Solution:
    ### 排序法 O(nlogn)
    def topKFrequent(self, nums, k):
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        # 对频率进行排序
        nums = sorted(d.items(), key=lambda x:x[1])

        res = []
        for i in range(len(nums)-1, len(nums)-k-1, -1):
            res.append(nums[i][0])

        return res

    ### 堆 O(nlogk)
    def topKFrequent(self, nums, k):
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        nums = list(d.items())
        
        # 最小堆-k个元素
        heap = []
        for i in range(k):
            heapq.heappush(heap, (nums[i][1], nums[i][0]))
        
        for i in range(k, len(nums)):
            if nums[i][1] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (nums[i][1], nums[i][0]))

        res = []
        for h in heap:
            res.append(h[1])

        return res


"""
数组
哈希表
分治
桶排序
计数
快速选择
排序
堆（优先队列）


"""

