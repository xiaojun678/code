class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort() # 原地排序
        s.sort()

        # 贪心算法：小饼干先喂饱小胃口
        # index = 0
        # for i in range(len(s)): # 循环饼干
        #     if s[i] >= g[index]:
        #         index += 1
        #     if index == len(g):
        #         break
        
        # return index
    
        # 贪心算法：大饼干先喂饱大胃口
        index = len(s) - 1
        num = 0
        for i in range(len(g)-1, -1, -1): # 循环胃口
            if index >= 0 and g[i] <= s[index]:
                index -= 1
                num += 1
        return num


s = Solution()
print(s.findContentChildren([1,2,3], [3]))

"""
贪心
数组
双指针
排序





"""
