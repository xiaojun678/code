class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j]：word1[0:i]转换成word2[0:j]的最少操作数
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        # 初始化
        for j in range(1, len(word2)+1):
            dp[0][j] = j # 插入
        for i in range(1, len(word1)+1):
            dp[i][0] = i # 删除
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 依次表示替换、删除和插入操作
                    # dp[i-1][j]：从 word1 中删除 word1[i-1]，再将word1 的前 i-1 个字符转换成 word2 的前 j 个字符
                    # dp[i][j-1]：将word1 的前 i 个字符转换成 word2 的前 j-1 个字符后，再插入一个字符
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[len(word1)][len(word2)]


"""
字符串
动态规划


"""