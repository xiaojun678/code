class Solution:
    def decodeString(self, s: str) -> str:
        # 括号内的状态， 字符，倍数
        stack, res, multi = [], "", 0
        for c in s:
            # 进栈
            if c == '[':
                stack.append([multi, res]) # 保存括号外倍数和过去所有的字符
                res, multi = "", 0 # 开始记录括号内的字符和倍数
            # 出栈
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c) # 连续多个数字     
            else:
                res += c
        return res




    ### 递归法
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)





s = Solution()
print(s.decodeString("3[a2[c]]"))

"""
栈
递归
字符串


"""