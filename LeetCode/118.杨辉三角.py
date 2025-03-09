class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]*i for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                # 数学含义
                # 从 i 个不同物品中选出 j 个物品的方案数
                # （1）选第i个物品：问题变成从剩下 i−1 个不同物品中选出 j−1 个物品的方案数
                # （2）不选第i个物品：问题变成从剩下 i−1 个不同物品中选出 j 个物品的方案数
                res[i][j] = res[i-1][j-1]+res[i-1][j]
        return res
        



"""
数组
动态规划


"""



