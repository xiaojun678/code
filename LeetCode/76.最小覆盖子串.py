from collections import Counter, defaultdict

class Solution(object):
    ### 滑动窗口
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans_left, ans_right = -1, len(s)
        cnt_s = Counter()  # s 子串字母的出现次数
        cnt_t = Counter(t)  # t 中字母的出现次数

        left = 0
        for right, c in enumerate(s):  # 移动子串右端点
            cnt_s[c] += 1  # 右端点字母移入子串
            while cnt_s >= cnt_t:  # 涵盖 Py3.10支持Counter比较大小
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                cnt_s[s[left]] -= 1  # 左端点字母移出子串
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]

    ### 不使用Counter方法
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)<len(t):
            return ''

        def check(d):
            # 因为是字母 所以这里时间复杂度最高是O(26) 不是O(n)
            for k in d.keys():
                if d[k]>0:
                    return False
            return True

        d_t = defaultdict(int)
        for w in t:
            d_t[w] += 1
        min_len = float('inf')
        min_s = ''
        left = right = 0
        n = len(s)

        # 时间窗口
        while right<n:
            if s[right] in d_t:
                d_t[s[right]] -= 1
            # 如果子串涵盖t，就不断移动左端点left直到不涵盖为止
            while check(d_t): # 检查子串包含的特定字母数是否大于等于目标串
                if min_len>right-left+1:
                    min_len = right-left+1
                    min_s = s[left:right+1]
                
                if s[left] in d_t:
                    d_t[s[left]]+=1
                left += 1  
            # 子串不涵盖t right继续向右扩充
            right+=1

        return min_s



s = Solution()
print(s.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))     

"""
哈希表
字符串
滑动窗口



"""
            

        