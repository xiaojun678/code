# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ### 快慢指针
        # 为什么一定会相遇？
        # 相对运动：假设慢指针不动，快指针相对走一步，则如果有环就一定会相遇
        slow = head
        fast = head
        while slow or fast:
            slow = slow.next
            if fast:
                if fast.next:
                    fast = fast.next.next
                else:
                    fast = None
            if slow == fast and fast:
                return True
        return False
    
"""
哈希表
链表
双指针


"""



