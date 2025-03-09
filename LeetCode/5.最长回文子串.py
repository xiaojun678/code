class Solution(object):
    ### 动态规划
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp[i][j]  [i, j]闭区间i,j是否是回文子串
        dp = [[0]*len(s) for _ in range(len(s))]
        max_length = 0
        max_str = ''
        for i in range(len(s)-1, -1, -1): # 逆序
            for j in range(i, len(s)):
                if s[i]==s[j]:
                    if j-i<=1: # 对应a aa情况
                        dp[i][j] = 1
                        max_length = max(max_length, j-i+1)
                        if max_length == j-i+1:
                            max_str = s[i:j+1][:]
                    else:
                        if dp[i+1][j-1]:
                            dp[i][j] = 1
                            max_length = max(max_length, j-i+1)
                            if max_length == j-i+1:
                                max_str = s[i:j+1][:]
        
        return max_str


    ### 中心扩展算法——选定一个回文中心，向左右两边扩展
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i) # 回文中心是一个数的情况-奇数回文串
            left2, right2 = self.expandAroundCenter(s, i, i + 1) # 回文中心是两个数的情况-偶数回文串
            # 记录最长串
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]






"""
双指针
字符串
动态规划


"""

