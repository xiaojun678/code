class Solution:
    def isPalindrome(self, s: str) -> bool:
        ### 简洁做法
        i, j = 0, len(s) - 1
        while i < j:
            # 左边不是字母数字 右移
            if not s[i].isalnum():
                i += 1
            # 右边不是字母数字 左移
            elif not s[j].isalnum():
                j -= 1
            # 都是字母数字 继续比较
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            # 都是字母数字但不相等
            else:
                return False
        return True

"""
双指针
字符串



作者：灵茶山艾府
链接：https://leetcode.cn/problems/valid-palindrome/solutions/3053284/jian-dan-ti-jian-dan-zuo-pythonjavaccgoj-1za0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
