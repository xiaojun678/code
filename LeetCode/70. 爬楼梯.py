import numpy as np


class Solution(object):
    ### 动态规划——空间优化版 时间复杂度O(n)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        pre, now = 1, 2 # 当前状态只和前两个状态有关 可对空间进行优化
        for i in range(2, n): # i=2时表示第3层台阶
            pre, now = now, pre+now
        return now

    ### 矩阵快速幂解法 时间复杂度O(logn)
    # https://leetcode.cn/problems/climbing-stairs/solutions/2560726/python3javacgotypescript-yi-ti-shuang-ji-27yo/
    # https://mp.weixin.qq.com/s/cv9Gd8NmEhXVrSiWeCvuWA
    # https://oi-wiki.org/math/binary-exponentiation/#__tabbed_1_2
    def climbStairs(self, n: int) -> int:
        res = np.array([(1, 1)]) # [1, 1]为初始状态
        factor = np.array([(1, 1), (1, 0)]) # 2*2矩阵，快速幂的底数
        n -= 1
        while n:
            if n & 1: # n为奇数时
                res = np.dot(res, factor)
            factor = np.dot(factor, factor)
            n >>= 1 # n除以2
        return int(res[0, 0])

s = Solution()
print(s.climbStairs(6))




"""
记忆化搜索
数学
动态规划



"""

