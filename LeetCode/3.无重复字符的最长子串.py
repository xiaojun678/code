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
        maxLen = 0
        left = 0

        for right in range(len(s)):
            while s[right] in d:
                d.remove(s[left])
                left += 1

            d.add(s[right])

            maxLen = max(right - left + 1, maxLen)
        
        return maxLen

s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))




"""
哈希表
字符串
滑动窗口


# 滑动窗口算法伪码框架
def slidingWindow(s: str):
    # 用合适的数据结构记录窗口中的数据，根据具体场景变通
    # 比如说，我想记录窗口中元素出现的次数，就用 map
    # 如果我想记录窗口中的元素和，就可以只用一个 int
    window = ...

    left, right = 0, 0
    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        window.add(c)
        # 增大窗口
        right += 1
        # 进行窗口内数据的一系列更新
        ...

        # *** debug 输出的位置 ***
        # 注意在最终的解法代码中不要 print
        # 因为 IO 操作很耗时，可能导致超时
        # print(f"window: [{left}, {right})")
        # ***********************

        # 判断左侧窗口是否要收缩
        while left < right and window needs shrink:
            # d 是将移出窗口的字符
            d = s[left]
            window.remove(d)
            # 缩小窗口
            left += 1
            # 进行窗口内数据的一系列更新
            ...




"""
