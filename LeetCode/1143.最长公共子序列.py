class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # dp[i][j]-text1[0:i]和text2[0:j]的最长公共子序列
        dp = [[0]*(len(text2)+1) for _ in range((len(text1)+1))]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[len(text1)][len(text2)]

"""
字符串
动态规划



"""