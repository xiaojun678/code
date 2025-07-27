class Solution:
    ### 双指针
    def isSubsequence(self, s: str, t: str) -> bool:
        l1, l2 = len(s), len(t)
        i, j = 0, 0

        while i < l1 and j < l2:
            if s[i] == t[j]:
                i += 1
            
            j += 1
        
        if i == l1:
            return True
        
        return False

    ### 动态规划 https://leetcode.cn/problems/is-subsequence/solutions/2813031/jian-ji-xie-fa-pythonjavaccgojsrust-by-e-mz22/
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        # t中下标>=i的最近字母c的下标 c不存在则为n
        nxt = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1): # 逆序
            nxt[i][:] = nxt[i + 1] # 继承上一个数
            nxt[i][ord(t[i]) - ord('a')] = i # 更新当前值

        # 这个写法无论 s 为空还是 t 为空，都能算出正确答案
        i = -1
        for c in s:
            i = nxt[i + 1][ord(c) - ord('a')]
            if i == n:  # c 不在 t 中，说明 s 不是 t 的子序列
                return False
        return True  # s 是 t 的子序列












"""
双指针
字符串
动态规划



"""