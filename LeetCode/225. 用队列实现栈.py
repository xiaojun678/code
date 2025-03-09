class MyQueue(object):
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        return self.size() == 0

### 一个队列的方法
class MyStack(object):

    def __init__(self):
        self.q1 = MyQueue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.push(x)


    def pop(self):
        """
        :rtype: int
        """
        # 通过先出队列 再进队列来取最后一个数
        # tips：可以在入栈时就进行调整 这样就只有push操作是O(n) 而pop和top均为O(1)
        size = self.q1.size()-1
        while size:
            temp = self.q1.pop()
            self.q1.push(temp)
            size -= 1
        return self.q1.pop()


    def top(self):
        """
        :rtype: int
        """
        temp = self.pop()
        self.q1.push(temp)
        return temp


    def empty(self):
        """
        :rtype: bool
        """
        return self.q1.size() == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



"""
栈
设计
队列

两个队列的方法：
第二个队列当作备份，即前n-1个先暂时移动到第2个队列 然后对第1个队列的元素进行出栈操作


"""