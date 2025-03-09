# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 反转链表
    def reverse(self, head, end):
        if head == end:
            return head
        p = head.next
        head.next = end.next

        while p:
            temp = p.next
            p.next = head

            if p == end:
                return end
            head = p
            p = temp

        return head

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        num = 1
        d_head = ListNode(0, head)
        start = d_head
        end = d_head.next

        while end:
            if num%k!=0:
                end = end.next
            else:
                temp1 = start.next
                temp2 = end.next
                start.next = self.reverse(start.next, end)
                start = temp1
                end = temp2
            num += 1
        
        return d_head.next


s = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

s.reverseKGroup(a, 1)






"""
递归
链表


递归解法：
https://leetcode.cn/problems/reverse-nodes-in-k-group/solutions/151616/di-gui-java-by-reedfan-2

"""