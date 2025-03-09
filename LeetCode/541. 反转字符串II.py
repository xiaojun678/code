class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        p = 0
        l = len(s)-1
        s_r = []
        while 1:
            if l-p>=2*k:
                s_r += list(reversed(s[p:p+k]))+s[p+k:p+2*k]
                p = p + 2*k
            elif l-p>=k:
                s_r += list(reversed(s[p:p+k]))+s[p+k:]
                break
            else:
                s_r += list(reversed(s[p:]))
                break
        return ''.join(s_r)


s = Solution()
print(s.reverseStr( "abcdefg", 1))


"""
双指针
字符串


原地反转字符串
-1切片反转字符串
对于python而言，右切片若超出最大长度则直接返回最大长度
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Two pointers. Another is inside the loop.
        p = 0
        while p < len(s):
            p2 = p + k
            # Written in this could be more pythonic.
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s
"""