class MinHeap(object):
    """
    小根堆
    """
    def __init__(self, nums):
        self.min_heap = nums
        # 建堆
        # 从顶至下堆化
        # 叶子节点无需堆化
        # len(nums)-1是最后一个叶子节点
        # 再减1整除2是得到父亲节点
        for i in range((len(nums)-1-1)//2, -1, -1):
            self.siftdown(i)

    # 从顶至下 堆化
    def siftdown(self, i):
        # 当前节点， 左右孩子
        mi, left, right = i, 2*i+1, 2*i+2
        if left<len(self.min_heap) and self.min_heap[left]<self.min_heap[mi]:
            mi, left = left, mi
        if right<len(self.min_heap) and self.min_heap[right]<self.min_heap[mi]:
            mi, right = right, mi
        
        if mi == i:
            return
        # 交换元素
        self.min_heap[i], self.min_heap[mi] = self.min_heap[mi], self.min_heap[i]
        
        # 继续堆化
        self.siftdown(mi)
    
    # 从下至顶 堆化
    def siftup(self, i):
        # 获取父亲
        parent = (i-1)//2

        if parent<0 or self.min_heap[parent]<=self.min_heap[i]:
            return
        
        # 交换元素
        self.min_heap[i], self.min_heap[parent] = self.min_heap[parent], self.min_heap[i]
        
        # 继续堆化
        self.siftup(parent)

    def push(self, val):
        self.min_heap.append(val)

        # 从下至顶堆化
        self.siftup(len(self.min_heap)-1)
    
    def pop(self):
        if not self.min_heap:
            print("堆为空")

        # 交换堆顶和最后一个元素
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
        # 弹出最后一个元素
        val = self.min_heap.pop()

        # 从顶至下堆化
        self.siftdown(0)

        return val

    def peek(self):
        return self.min_heap[0]

class Solution(object):
    ### 堆
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 前k个元素进堆
        heap = MinHeap(nums[:k])

        # 从第k+1个元素开始 依次弹出小元素 大元素进堆
        for i in range(k, len(nums)):
            if heap.peek() < nums[i]:
                # 弹出堆顶最小元素
                heap.pop()
                # 加入当前大的元素
                heap.push(nums[i])
        # 堆顶即第k大的元素
        return heap.peek()

    ### 三路快排——避免存在众多重复元素的情况
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            # 基准数
            pivot = nums[0]
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - len(nums) + len(small))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot
        
        return quick_select(nums, k)

    ### 普通快排——时间超时
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickSort(left, right):
            if left>=right:
                return
           # 锚点
            tmp = nums[left]
            l, r = left, right
            while l < r:
                while l < r and nums[r]>=tmp:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l]<tmp:
                    l += 1
                nums[r] = nums[l]
            
            mid = l
            nums[mid] = tmp
            # 第k大的元素已找到
            if mid == len(nums)-k:
                return
            
            if mid > len(nums)-k:
                quickSort(left, mid-1)
            else:
                quickSort(mid+1, right)
        
        quickSort(0, len(nums)-1)

        return nums[len(nums)-k]

"""
数组
分治
快速选择
排序
堆（优先队列）


"""