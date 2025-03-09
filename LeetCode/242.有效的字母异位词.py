class Solution(object):
    ### 记录字母出现的次数
    # 时间复杂度O(n) 空间复杂度O(1)
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = {} # 记录字母出现的次数
        for i, _ in enumerate(s):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            if t[i] in d:
                d[t[i]] -= 1
            else:
                d[t[i]] = -1
        for key in d.keys():
            if d[key]!=0:
                return False
        return True



s = Solution()
print(s.isAnagram( "anagram","nagaram"))


"""
哈希表
字符串
排序



"""


