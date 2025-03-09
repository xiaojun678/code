class Solution:
    ### 双指针做法 空间复杂度O(n)
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            # 搜索首个空格
            while i >= 0 and s[i] != ' ': 
                i -= 1 
            
            # 添加单词
            res.append(s[i + 1: j + 1]) 
            
            # 跳过单词间空格
            while i >= 0 and s[i] == ' ': 
                i -= 1 
            
            j = i # j 指向下个单词的尾字符
        
        return ' '.join(res) # 拼接并返回

"""
双指针
字符串


Python简洁做法（面试不推荐）：
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()         # 删除首尾空格
        strs = s.split()      # 分割字符串
        strs.reverse()        # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回

"""
