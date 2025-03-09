from collections import defaultdict

class Solution(object):
    ### 贪心法
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # 给字母计数
        d = defaultdict(int)
        for w in s:
            d[w] += 1
        
        path = []
        res = []
        for i in range(len(s)):
            path.append(s[i])
            d[s[i]] -= 1
            
            # 截断条件：当前子串中的任意一个字符在剩余子串中均不存在
            flag = True
            for w in path:
                if d[w] > 0:
                    flag = False
                    break
            if flag:
                res.append(len(path))
                path = []
        
        return res
    
    ### 优化版——本质是合并区间！
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(s)}  # 每个字母最后出现的下标
        ans = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])  # 更新当前区间右端点的最大值
            if end == i:  # 当前区间合并完毕
                ans.append(end - start + 1)  # 区间长度加入答案
                start = i + 1  # 下一个区间的左端点
        return ans
    

"""
贪心
哈希表
双指针
字符串


"""