class Solution(object):
    ### 一般解法
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     d = []
    #     maxLen = 0
    #     for w in s:
    #         if w in d:
    #             idx = d.index(w)
    #             d = d[idx+1:]
    #         d.append(w)
    #         maxLen = max(maxLen, len(d))
    #     return maxLen

    ### 滑动窗口
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = set()
        maxLen = length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in d:
                d.remove(s[left])
                left += 1
                length -= 1

            d.add(s[right])
            length += 1

            maxLen = max(length, maxLen)
        
        return maxLen

s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))




"""
哈希表
字符串
滑动窗口



滑动窗口解题模板：
//外层循环扩展右边界，内层循环扩展左边界
for (int l = 0, r = 0 ; r < n ; r++) {
	//当前考虑的元素
	while (l <= r && check()) {//区间[left,right]不符合题意
        //扩展左边界
    }
    //区间[left,right]符合题意，统计相关信息
}




"""
