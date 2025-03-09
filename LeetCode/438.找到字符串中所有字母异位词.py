class Solution(object):
    ### 滑动窗口
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d_p = {}
        d_s = {}
        for i in range(97, 123):
            d_p[chr(i)] = d_s[chr(i)] = 0

        for w in p:
            d_p[w] += 1
        for w in s[:len(p)]:
            d_s[w] += 1

        ans = []
        left = 0
        right = len(p)-1

        while right<len(s):
            if d_s == d_p:
                ans.append(left)

            if right == len(s)-1:
                break

            d_s[s[left]] -= 1
            left += 1

            right += 1
            d_s[s[right]] += 1

        return ans


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
