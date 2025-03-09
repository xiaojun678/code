class Solution:
    ### 回溯法
    def combinationSum(self, candidates, target):
        res = []
        path = []

        def digui(path, start):
            sums = sum(path)

            if sums == target:
                res.append(path[:])

            for i in range(start, len(candidates)):
                if sums + candidates[i] <= target:
                    path.append(candidates[i])
                    # 确保不往回访问
                    digui(path, i) # i而不是i+1保证可以重复访问

                    path.pop()
        
        digui(path, 0)

        return res

    ### 动态规划 - 完全背包
    # https://leetcode.cn/problems/combination-sum/solutions/406900/bei-bao-wen-ti-zi-dian-by-gsp_leetcode
    def combinationSum(self, candidates, target: int):
        dp = {i:[] for i in range(target+1)}
        dp[0] = [[]]
        # 物品
        for num in candidates:
            # 背包
            for i in range(num, target+1): # 从num开始
                if dp[i-num]:
                    for a in dp[i-num]:
                        dp[i].append([num]+a)
        return dp[target]




"""
数组
回溯

"""