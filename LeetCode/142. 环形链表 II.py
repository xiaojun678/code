# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def detectCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     s = set()
    #     while head:
    #         if head not in s:
    #             s.add(head)
    #         else:
    #             return head
    #         head = head.next
    #     return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        设链表共有 a+b 个节点，其中 链表头部到链表入口 有 a 个节点（不计链表入口节点）， 链表环 有 b 个节点（这里需要注意，a 和 b 是未知数）
        设两指针分别走了 f，s 步，则有：
        1. fast 走的步数是 slow 步数的 2 倍，即 f=2s（解析： fast 每轮走 2 步）
        2. fast 比 slow 多走了 n 个环的长度，即 f=s+nb（ 解析： 双指针都走过 a 步，然后在环内绕圈直到重合，重合时 fast 比 slow 多走 环的长度整数倍 ）。
        
        知s=nb, f=2nb
        若让此时f指向head，则f和s相遇时走的路径为：f'=a s=nb+a
        即为入口
        """
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        
        fast = head
        while fast!=slow:
            fast = fast.next
            slow = slow.next
        return slow

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

a.next = b
b.next = c
c.next = d
d.next = b

s = Solution()
s.detectCycle(a)




"""
哈希表
链表
双指针







"""


