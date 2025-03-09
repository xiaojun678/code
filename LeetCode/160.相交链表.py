# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def getIntersectionNode(self, headA, headB):
    #     """
    #     :type head1, head1: ListNode
    #     :rtype: ListNode
    #     """
    #     m = n = 0
    #     p = headA
    #     while p:
    #         m+=1
    #         p = p.next
    #     p = headB
    #     while p:
    #         n+=1
    #         p = p.next
        
    #     diff = abs(m-n)
    #     # 第一个单链表先跑
    #     if m>n:
    #         while diff!=0:
    #             headA = headA.next
    #             diff -= 1
    #     # 第二个链表先跑
    #     else:
    #         while diff!=0:
    #             headB = headB.next
    #             diff -= 1
        
    #     while headA:
    #         if headA==headB:
    #             return headA
    #         headA = headA.next
    #         headB = headB.next
    #     return None
    
    ### 双指针做法
    # 指针A、B同时走
    # 指针A把A走完后走B  指针B把B走完后走A
    # 如果A和B有相交点 则会在相交的第一个节点相遇
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A, B = headA, headB

        # 如果不相交 那么A和B最后一定会同时为空（走了A的长度+B的长度）
        while A or B:
            if A == B:
                return A
            A = A.next if A else headB
            B = B.next if B else headA
        return None



"""
哈希表
链表
双指针



"""
