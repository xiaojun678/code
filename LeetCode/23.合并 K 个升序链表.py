# Definition for singly-linked list.
import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKTwo(self, head1, head2):
        d_head = ListNode()
        p = d_head
        while head1 or head2:
            if head1 and head2:
                if head1.val<=head2.val:
                    p.next = head1
                    head1 = head1.next
                else:
                    p.next = head2
                    head2 = head2.next
                p = p.next
            elif head1:
                p.next = head1
                return d_head.next
            else:
                p.next = head2
                return d_head.next
        return d_head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # 分治法 类似归并排序
        m = len(lists)
        if m == 0: return None  # 注意输入的 lists 可能是空的
        if m == 1: return lists[0]  # 无需合并，直接返回
        left = self.mergeKLists(lists[:m // 2])  # 合并左半部分
        right = self.mergeKLists(lists[m // 2:])  # 合并右半部分
        return self.mergeKTwo(left, right)  # 最后把左半和右半合并

    # 优先级队列（使用堆实现）
    def mergeKLists(self, lists):
        import heapq
        dummy = ListNode(0)
        p = dummy
        heap = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(heap, (lists[i].val, i)) # 同时把下标和值加进去
                lists[i] = lists[i].next
        while heap:
            val, idx = heapq.heappop(heap)
            p.next = ListNode(val)
            p = p.next
            # 某个下标pop出去一个 相应的就要再push一个
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next



"""
链表
分治
堆（优先队列）
归并排序


"""



