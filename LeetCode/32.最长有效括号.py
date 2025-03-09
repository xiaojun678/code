class Solution(object):
    ### 简单做法
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [0]*len(s)

        # 配对的地方赋1
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or not stack:
                stack.append(i)
            else:
                if s[stack[-1]] == '(': # 配对成功
                    idx = stack.pop()
                    d[idx] = d[i] = 1
                else:
                    stack.append(i)
        
        # 最长有效括号即为连续为1的最长长度
        max_num = num = 0
        for x in d:
            if x:
                num += 1
            else:
                num = 0
            
            max_num = max(max_num, num)
        
        return max_num

    ### 动态规划
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:
            return 0
        # 包含第i个字符的最长有效子串
        dp = [0]
        
        # https://leetcode.cn/problems/longest-valid-parentheses/solutions/206995/dong-tai-gui-hua-si-lu-xiang-jie-c-by-zhanganan042
        stack = [0] # 这里可以不需要 然后把状态转移部分换成i - dp[i - 1] - 2

        for i in range(1, len(s)):
            if s[i] == '(' or not stack:
                dp.append(0)
                stack.append(i)
            else:
                if s[stack[-1]]=='(':
                    idx = stack.pop()
                    # )()())  (()()) 
                    # 最长长度=对应另一半元素的前一个长度+当前上一个元素长度+2
                    dp.append(2+dp[max(idx-1, 0)]+dp[i-1])
                else:
                    dp.append(0)
                    stack.append(i)

        return max(dp)













"""
栈
字符串
动态规划



"""
