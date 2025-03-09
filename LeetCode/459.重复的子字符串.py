class Solution(object):
    ### 暴力解法：时间复杂度O(n)
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 判断s是否可全部由子串son构成
        def repeatedSon(s, son):
            idx = 0
            k = len(son)
            while idx < len(s):
                if s[idx:idx+k] != son:
                    return False
                idx += k
            if idx > len(s):
                return False
            return True
        # 循环遍历子串
        k = len(s)//2 + 1
        for i in range(1, k+1):
            # 自身不是子串
            if i < len(s) and repeatedSon(s, s[:i]):
                return True
        
        return False



"""
字符串
字符串匹配


"""