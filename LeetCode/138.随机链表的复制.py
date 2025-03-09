# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    ### 借助哈希表：空间复杂度O(n)
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 旧节点-新节点映射
        d = {}

        p = head
        h_new = Node(0)
        p_new = h_new
        while p:
            p_new.next = Node(p.val)
            p_new = p_new.next
            d[p] = p_new
            p = p.next
        
        p = head
        while p:
            if p.random:
                d[p].random = d[p.random]
            else:
                d[p].random = None

            p = p.next

        return h_new.next
    
    ### 空间复杂度O(1)做法 思路见下
    def copyRandomList(self, head):
        if head is None:
            return None

        # 复制每个节点，把新节点直接插到原节点的后面  原节点 1 -> 新节点 1
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        # 遍历交错链表中的原链表节点
        cur = head
        while cur:
            if cur.random:
                # 要复制的 random 是 cur.random 的下一个节点
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 遍历交错链表中的新链表节点
        cur = head.next
        while cur.next:
            # 删除原链表的节点，即当前节点的下一个节点
            cur.next = cur.next.next
            cur = cur.next

        # 返回 head.next 就相当于删除了原链表的头节点
        return head.next



"""
哈希表
链表



哈希表的空间复杂度为O(n)，下面介绍空间复杂度为O(1)的方法：
在原有链表基础上构建拼接链表：原节点 1 -> 新节点 1 -> 原节点 2 -> 新节点 2 -> ……
新节点是原节点的深拷贝

这样，我们可以直接找到每一个拷贝节点的随机指针应当指向的节点，
即为其原节点 S 的随机指针指向的节点 T 的后继节点 T 
需要注意原节点的随机指针可能为空，需要特别判断这种情况

最后再拆分拼接链表：即将原链表和新链表拆分开，返回新链表即可

https://leetcode.cn/problems/copy-list-with-random-pointer/solutions/2361362/138-fu-zhi-dai-sui-ji-zhi-zhen-de-lian-b-6jeo
"""

