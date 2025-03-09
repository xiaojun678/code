class Solution:
    """
    多数元素（超过一半）必定是比其他元素多的，遍历一次对比前后元素，不相同则相互消去，剩下的就是多数元素。

    摩尔投票法： 
    初始时，设置多数元素为nums[0], 多数元素计数为count=1。
    遍历集合，如果元素与多数元素相同，则递增多数元素计数，继续遍历；
    如果不相同，则递减多数元素计数，同时如果递减后计数=0，那么就将当前元素设置为多数元素。
    只有这样，才不会错过多数元素，并且，最后求出来的一定是多数元素，并且复杂度为O(n),空间复杂度为O(1)
    """
    def majorityElement(self, nums):
        # 摩尔投票法
        flag = nums[0]
        score = 1
        for i in range(1, len(nums)):
            if score <= 0:
                score = 1
                flag = nums[i]
                continue

            if nums[i] == flag:
                score += 1
            else:
                score -= 1
        
        return flag



"""
数组
哈希表
分治
计数
排序


"""