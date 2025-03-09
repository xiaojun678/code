class Solution(object):
    ### 动态规划
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = list() # n状态只和n-1和n-2的状态有关 所以此题不需要使用列表 使用2个变量即可
        dp.append(0)
        dp.append(1)
        for i in range(2, n+1):
            dp.append(dp[i-1]+dp[i-2])
        
        return dp[n]
    ### 递归
    # def fib(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
        
    #     return self.fib(n-1)+self.fib(n-2)


s = Solution()
print(s.fib(4))


"""






"""



