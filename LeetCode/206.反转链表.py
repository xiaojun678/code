# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # ### 迭代法
    # def reverseList(self, head):
    #     """
    #     :type head: Optional[ListNode]
    #     :rtype: Optional[ListNode]
    #     """
    #     if not head:
    #         return head
    #     p = head.next

    #     head.next = None # 这个不可缺少 不然会形成死循环

    #     while p:
    #         temp = p.next
    #         p.next = head
    #         head = p
    #         p = temp

    #     return head

    ### 递归法
    # https://leetcode.cn/problems/reverse-linked-list/solutions/2361282/206-fan-zhuan-lian-biao-shuang-zhi-zhen-r1jel
    def reverseList(self, head) :
        def recur(cur, pre):
            if not cur: 
                return pre     # 终止条件
            res = recur(cur.next, cur) # 递归后继节点
            cur.next = pre             # 修改节点引用指向
            return res                 # 返回反转链表的头节点
        
        return recur(head, None)       # 调用递归并返回


a = ListNode(1)
a.next = ListNode(2)

s = Solution()
s.reverseList(a)
