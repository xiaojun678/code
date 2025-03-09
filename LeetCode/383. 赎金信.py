from collections import defaultdict

class Solution(object):
    ### 哈希表判断字符出现次数
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 记录magazine字符串的字符数量
        nums = defaultdict(int)
        for m in magazine:
            nums[m] += 1
        
        # 判断magazine中的字符数是否大于等于ransomNote
        for r in ransomNote:
            if r not in nums or nums[r] <= 0:
                return False
            nums[r] -= 1
        
        return True



"""
哈希表
字符串
计数

哈希表做法中可以直接使用数组来代替字典，index为小写字母的ascii码
"""
