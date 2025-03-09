from heapq import *

### 借助一个大顶堆和小顶堆
class MedianFinder:
    # https://leetcode.cn/problems/find-median-from-data-stream/solutions/2361972/295-shu-ju-liu-de-zhong-wei-shu-dui-qing-gmdo/
    def __init__(self):
        # A 保存较大的一半，长度为2/N（N为偶数）或 N+1/2（N为奇数）
        self.A = [] # 小顶堆，保存较大的一半
        # B 保存较小的一半，长度为2/N（N为偶数）或 N-1/2（N为奇数）
        self.B = [] # 大顶堆，保存较小的一半

    def addNum(self, num):
        # 此时为奇数
        if len(self.A) != len(self.B):
            heappush(self.A, num) # A先进
            heappush(self.B, -heappop(self.A)) # A再把最小的一个数给B 最后是相当于B加了一个数
        # 此时为偶数
        else:
            heappush(self.B, -num) # B先进
            heappush(self.A, -heappop(self.B)) # B再把最大的一个数给A 最后是相当于A加了一个数

    def findMedian(self):
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0      


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


"""
设计
双指针
数据流
排序
堆（优先队列）



"""

