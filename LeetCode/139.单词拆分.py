class Solution(object):
    ### 完全背包——排列版
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] 表示字符串的前 i 个字符是否可以被拆分成单词
        dp[0] = True  # 初始状态，空字符串可以被拆分成单词

        for i in range(1, n + 1): # 遍历背包
            for j in range(i): # 遍历单词
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True  # 如果 s[0:j] 可以被拆分成单词，并且 s[j:i] 在单词集合中存在，则 s[0:i] 可以被拆分成单词
                    break

        return dp[n]


    ### 常规动态规划
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 记录前多少字符可以拼出来
        dp = [-1] # -1是从0开始的字符串

        wordDict = set(wordDict)
        for i in range(len(s)):
            # 从某个字符到当前字符是否存在
            for d in dp:
                if s[d+1:i+1] in wordDict:
                    dp.append(i)
                    break
        return dp[-1] == (len(s)-1)





"""
如果求组合数就是外层for循环遍历物品，内层for遍历背包。
如果求排列数就是外层for遍历背包，内层for循环遍历物品。

在这里做一个总结：
求组合数：动态规划：518.零钱兑换II
求排列数：动态规划：377. 组合总和 Ⅳ、动态规划：70. 爬楼梯进阶版（完全背包）
求最小数：动态规划：322. 零钱兑换、动态规划：279.完全平方数

https://www.programmercarl.com/0139.%E5%8D%95%E8%AF%8D%E6%8B%86%E5%88%86.html#%E6%80%9D%E8%B7%AF
https://leetcode.cn/problems/word-break/solutions/744153/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-kchg9
"""


"""
字典树
记忆化搜索
数组
哈希表
字符串
动态规划




"""

