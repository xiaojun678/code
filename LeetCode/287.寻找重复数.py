class Solution:
    ### 标记法 修改了nums数组
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                return abs(nums[i])
            
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]


    ### 按照区间内的数量进行二分法查找 O(nlogn)
    def findDuplicate(self, nums):
        # 1, n
        left, right = 1, len(nums)-1
        while left < right:
            mid = (left+right)//2
            # 分别统计[left, mid]和[mid+1, right]的数量
            num1 = 0
            num2 = 0
            for num in nums:
                if left <= num <= mid:
                    num1+=1
                if mid+1 <= num <= right:
                    num2+=1
            # 某个区间内的数量超出区间范围  说明这个区间存在重复数
            if num1 > mid+1-left:
                right = mid
            else:
                left = mid+1
        
        return left
    
    ### 快慢指针：环形链表 O(n)
    def findDuplicate(self, nums):
        # 将下标和对应数值看成链表，这样就构成了从0到n的环形链表，环的入口即为重复值
        """
        对于[1,3,4,2,2]：0->1->3->2->4->2
        """
        slow = fast = 0 # 从0开始

        while 1:
            # 快指针走两次
            fast = nums[fast]
            fast = nums[fast]
            # 慢指针走一次
            slow = nums[slow]

            if fast == slow:
                break
        
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return fast


"""
https://leetcode.cn/problems/find-the-duplicate-number/solutions/2833858/cong-er-fen-cha-zhao-dao-kuai-man-zhi-zh-ixa3
位运算
数组
双指针
二分查找



"""



