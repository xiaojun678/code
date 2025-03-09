class ListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.num = 0
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= self.num:
            return -1
        p = self.head
        for _ in range(index):
            p = p.next
        return p.val


    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        temp = ListNode(val, self.head)
        self.head = temp
        self.num += 1


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.num == 0:
            self.addAtHead(val)
            return
        temp = ListNode(val, None)
        p = self.head
        for _ in range(self.num-1):
            p = p.next
        p.next = temp
        self.num +=1


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.num:
            return
        # 虚拟头方法
        dp = ListNode(-1, self.head)
        temp = ListNode(val)
        p = dp
        for _ in range(index):
            p = p.next
        temp.next = p.next
        p.next = temp
        self.num += 1
        self.head = dp.next


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.num:# 超出边界
            return
        # 虚拟头方法
        dp = ListNode(-1,self.head)
        p = dp
        for _ in range(index):
            p = p.next
        self.num -= 1
        p.next = p.next.next
        self.head = dp.next


# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)
myLinkedList.get(1)
myLinkedList.deleteAtIndex(1)
myLinkedList.get(1)
myLinkedList.get(3)
myLinkedList.deleteAtIndex(3)
myLinkedList.deleteAtIndex(0)
myLinkedList.get(0)
myLinkedList.deleteAtIndex(0)
myLinkedList.get(0)


"""
添加一个虚拟头会方便很多
1.如果只看返回的结果，如本题，那么不需要管虚拟头
2.如果需要原地修改链表，则在利用完虚拟头后需要返回的是链表的真head


"""