# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    ### 模拟写法
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 记录进位
        num = 0
        head = ListNode() # 空节点
        p = head
        while l1 or l2:
            t1 = t2 = 0
            if l1:
                t1 = l1.val
                l1 = l1.next
            if l2:
                t2 = l2.val
                l2 = l2.next      

            p.next = ListNode((t1+t2+num)%10)
            num = (t1+t2+num)//10
            p = p.next

            if (not l1) and (not l2) and num:
                p.next = ListNode(num)

        return head.next
    
    ### 递归写法
    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwoNumbers(self, l1, l2, carry=0):
        if l1 is None and l2 is None:  # 递归边界：l1 和 l2 都是空节点
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        s = carry + l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = s % 10  # 每个节点保存一个数位（直接修改原链表）
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s // 10)  # 进位
        return l1


s = Solution()
a = ListNode(9, ListNode(9,ListNode(9)))
b = ListNode(9, ListNode(9))

h = s.addTwoNumbers(a,b)

while h:
    print(h.val)
    h = h.next

"""
递归
链表
数学




"""


