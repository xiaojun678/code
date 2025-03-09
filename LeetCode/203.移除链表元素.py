class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val: # 移除头结点
            head = head.next
        p = head # 此结点一定不等于特定值
        while p and p.next: # 连续两个结点一定存在
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head


a = [1,1,7,7]
head = ListNode()
p = head
for i, val in enumerate(a):
    p.val = val
    if i == len(a)-1:
        p.next = None
    else:
        temp = ListNode()
        p.next = temp
        p = p.next

s = Solution()
p = s.removeElements(head, 7)
while p:
    print(p.val)
    p = p.next


"""
移除头结点的方法：
1.提前移除，如上
2.设置虚拟头结点，并指向head，最终返回虚拟头结点的next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next = head)
        
        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next
3.使用递归操作


"""