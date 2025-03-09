class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums) # 去重

        for num in num_set:
            if num - 1 not in num_set: # 确保num是第一个枚举的 即不存在num-1的数
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set: # 访问集合的时间复杂度为O(1)
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


s = Solution()

nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(s.longestConsecutive(nums))
            

"""
并查集
数组
哈希表

python中的字典和集合是基于哈希表实现的，查看一个数的时间复杂度为O(1)
https://www.cnblogs.com/videvops/articles/15774274.html
"""

