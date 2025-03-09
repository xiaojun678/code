class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        return s
    

s = Solution()
print(s.reverseString(['h','e','l','l','o']))
        
"""
双指针
字符串

一些python反转的操作：
s[:] = reversed(s)
s[:] = s[::-1]
s[:] = [s[i] for i in range(len(s) - 1, -1, -1)]
s.reverse()
"""

