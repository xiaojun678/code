class Solution(object):
    ### 双指针法：时间复杂度O(m+n)
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1 # nums1有数的结尾
        p2 = n - 1 # nums2有数的结尾

        tail = m + n -1 # nums1空间的结尾

        while p1 >= 0 or p2 >= 0:
            # 到达nums1的第一个位置
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            # 到达nums2的第一个位置
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[p1], nums1[tail] = nums1[tail], nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            
            tail -= 1



"""
数组
双指针
排序


"""