# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        num = 1
        slow = fast = head
        pre = head
        while fast.next:
            if num == n:
                pre = slow
                slow = slow.next
                fast = fast.next
            if num < n:
                fast = fast.next
                num += 1
        # 加个虚拟头结点会简单
        if slow == head:
            return head.next
        pre.next = slow.next
        return head

"""
链表
双指针


"""


