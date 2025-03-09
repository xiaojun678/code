# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        # 虚拟头结点
        h = ListNode(0, head)
        prev = h
        nex = head.next
        num = 0
        while nex:
            if num%2==0:
                temp1 = prev.next
                temp2 = nex.next
                prev.next = nex
                nex.next = temp1
                temp1.next = temp2

                prev = temp1
                nex = temp2
            else:
                nex = nex.next          
            num += 1

        return h.next

    ### 递归法
    def swapPairs(self, head):
        if head is None or head.next is None:  # 递归边界
            return head  # 不足两个节点，无需交换

        node1 = head
        node2 = head.next
        node3 = node2.next

        node1.next = self.swapPairs(node3)  # 1 指向递归返回的链表头
        node2.next = node1  # 2 指向 1

        return node2  # 返回交换后的链表头节点

"""
递归
链表

"""

