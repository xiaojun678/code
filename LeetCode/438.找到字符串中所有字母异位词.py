class Solution:
    def judge(self, s_l, p_l):
        for i in range(26):
            if s_l[i] > p_l[i]:
                return True
        return False

    ### 滑动窗口法
    def findAnagrams(self, s: str, p: str):
        s_list = [0]*26
        p_list = [0]*26
        res = []

        for w in p:
            p_list[ord(w)-ord('a')] += 1
        
        left = right = 0

        while right < len(s):
            s_list[ord(s[right])-ord('a')] += 1
            right += 1

            # 收缩窗口
            while self.judge(s_list, p_list):
                s_list[ord(s[left])-ord('a')] -= 1
                left += 1
            
            if s_list == p_list:
                res.append(left)

        return res


    ### 一般解法 - 超时
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p = sorted(p)
        ans = []
        for idx in range(len(s)-len(p)+1):
            if sorted(s[idx:idx+len(p)]) == p:
                ans.append(idx)
        return ans



s = Solution()
print(s.findAnagrams("abab", 'ab'))


"""
哈希表
字符串
滑动窗口


1.可以不用哈希表存子串  用列表即可 下标表示字母的ASCII码
2.进一步，也可以维护一个列表 遍历到每个字母时判断diff是否等于0

https://leetcode.cn/problems/find-all-anagrams-in-a-string/solutions/1123971/zhao-dao-zi-fu-chuan-zhong-suo-you-zi-mu-xzin

"""
