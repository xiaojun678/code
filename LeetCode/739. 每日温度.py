class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = []
        # 单调递增栈（从底到顶）
        stack = [] # 只存元素下标即可

        for i in range(len(temperatures)-1, -1, -1): # 从右到左
            while len(stack) and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if len(stack):
                res.append(stack[-1]-i)
            else:
                res.append(0)
            stack.append(i)

        
        return res[::-1]
    

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))


"""
栈
数组
单调栈




"""

