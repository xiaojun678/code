class Solution(object):
    ### 暴力解法 时间复杂度O(nm)
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        
        return -1
    
    ### KMP算法 时间复杂度O(n+m)
    # https://www.programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html
    # 获取next数组-模板串各个位置的最长相等前后缀
    def getNext(self, s):
        next = [0]*len(s)

        # 两个指针i和j，j指向前缀末尾位置，i指向后缀末尾位置
        j = -1
        next[0] = j

        for i in range(1, len(s)):
            # 前后缀不相同
            while j >= 0 and s[i] != s[j+1]:
                j = next[j] # 向前回溯
            
            # 找到相同的前后缀
            if s[i] == s[j+1]:
                j += 1
            
            # 将j（前缀的长度）赋给next[i]
            next[i] = j
        
        return next

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 获取next数组
        next = self.getNext(needle)
        # 定义两个下标-j指向模式串起始位置，i指向文本串起始位置
        j = -1 # 因为next数组里记录的起始位置为-1
        for i in range(len(haystack)):
            # 不匹配
            while j >= 0 and haystack[i] != needle[j+1]:
                j = next[j] # j 寻找之前匹配的位置
            
            # 匹配，j和i同时向后移动
            if haystack[i] == needle[j+1]:
                j += 1
            
            # 文本串s里出现了模式串t
            if j == len(needle) - 1:
                return i - len(needle) + 1

        return -1





"""
双指针
字符串
字符串匹配

KMP算法原理：
https://www.programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html
https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/575568/shua-chuan-lc-shuang-bai-po-su-jie-fa-km-tb86

"""



