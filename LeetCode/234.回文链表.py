# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head) -> bool:
        # 找中间节点
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 从中间节点开始反转链表
        p1 = slow
        p2 = slow.next
        p1.next = None

        while p2:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        # 判断前半段链表和后半段链表是否相同
        while head and p1:
            if head.val != p1.val:
                return False
            head = head.next
            p1 = p1.next
        return True

"""
栈
递归
链表
双指针



"""

