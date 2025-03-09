class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(nums)
        # 单调栈
        stack = []
        num = 0
        index = 0
        while 1: # 可以使用for循环来控制循环两次
            while len(stack) and nums[index]>nums[stack[-1]]:
                res[stack[-1]] = nums[index]
                stack.pop()
            
            stack.append(index)

            if index == len(nums)-1: # 记录循环次数
                num += 1
            if num >= 2: # 循环两次 强制退出
                break
            index = (index+1)%(len(nums)) # 循环 也可以直接把两个数组拼接在一起！
        return res

s = Solution()
print(s.nextGreaterElements([1,1,1,1,1]))



"""
栈
数组
单调栈



"""