class Solution(object):
    ### 栈
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for w in s:
            if not stack or stack[-1] != w:
                stack.append(w)
            else:
                stack.pop()
        
        return ''.join(stack)

    ### 双指针
    def removeDuplicates(self, s):
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]
            
            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
            
        return ''.join(res[0: slow])


"""
栈
字符串

"""