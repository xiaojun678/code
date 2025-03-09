class Node(object):
    # 双向链表 以维护最近使用：越靠近head就越久被使用
    def __init__(self,key = 0,  val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.length = 0
        # 第一个节点是最久被使用 最后一个节点是最新使用
        self.head = Node() # 空头节点
        self.last = self.head # 记录最后一个节点
        self.d = {} # 键是key 值是节点

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            if self.d[key]!=self.last:  # 如果更新节点不是最后一个节点
                # 更新最新使用
                cur = self.d[key]
                pre = cur.prev
                nex = cur.next

                pre.next = nex
                nex.prev = pre
                
                cur.prev = self.last
                self.last.next = cur
                cur.next = None

                self.last = cur

            return self.d[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.d:
            p = Node(key, value)
            self.last.next = p
            p.prev = self.last

            self.last = p

            self.d[key] = p
            self.length += 1

            if self.length > self.capacity:
                # 移除第一个节点
                cur = self.head.next
                
                self.head.next = cur.next
                cur.next.prev = self.head

                del self.d[cur.key]
                self.length -= 1

        else:
            self.d[key].val = value
            if self.d[key]!=self.last:  # 如果更新节点不是最后一个节点
                # 更新最新使用
                cur = self.d[key]
                pre = cur.prev
                nex = cur.next

                pre.next = nex
                nex.prev = pre
                
                cur.prev = self.last
                self.last.next = cur
                cur.next = None
                
                self.last = cur

"""
设计
哈希表
链表
双向链表


"""


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
obj.put(1,1)
obj.put(2,2)
obj.put(3,3)
print(obj.get(1))
print(obj.get(3))
print(obj.get(2))
obj.put(4,4)
print(obj.get(2))