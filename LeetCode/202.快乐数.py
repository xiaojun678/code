class Solution(object):
    """
    使用哈希法，来判断这个sum是否重复出现，如果重复了就是return false， 否则一直找到sum为1为止
    """
    def square(self, num):
        l = len(str(num))
        sum = 0
        for _ in range(l):
            sum += (num%10)*(num%10)
            num = (num - num%10)/10
        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set()
        while 1:
            n = self.square(n)
            if n == 1:
                return True
            if n in d: # 出现循环 不是快乐数
                return False
            d.add(n)

s = Solution()
print(s.isHappy(2))


"""
哈希表
数学
双指针

本题的重点是要清楚有几种可能：
1.最终会得到 1。
2.最终会进入循环。
（1）返回的结果为1，True
（2）如果它不在哈希集合中，我们应该添加它。
（3）如果它在哈希集合中，这意味着我们处于一个循环中，因此应该返回 false。

还可以使用快慢指针法用来检测依次返回的结果（构成链表）是否存在环
慢指针每次前行一次 快指针每次前行两次 如果存在环就一定会相遇
"""