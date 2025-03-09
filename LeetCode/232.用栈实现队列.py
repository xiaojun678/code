class MyStack(object):

    def __init__(self):
        self.ls = []
    def size(self):
        return len(self.ls)
    
    def is_empty(self):
        return len(self.ls) == 0
    
    def push(self,val):
        self.ls.insert(0, val)

    def pop(self):
        return self.ls.pop(0)
    
    def print(self):
        print(str(self.ls))

# class MyQueue(object):

#     def __init__(self):
#         self.s1 = MyStack() # 有数
#         self.s2 = MyStack() # 无数

#     def transfer(self, type): # 单个操作时间复杂度O(2n)
#         while self.s1.size():
#             self.s2.push(self.s1.pop())
        
#         temp = self.s2.pop()
#         if type == 'peek':
#             self.s1.push(temp)

#         while self.s2.size():
#             self.s1.push(self.s2.pop())
        
#         return temp


#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.s1.push(x)


#     def pop(self):
#         """
#         :rtype: int
#         """
#         return self.transfer('pop')


#     def peek(self):
#         """
#         :rtype: int
#         """
#         return self.transfer('peek')


#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return self.s1.size() == 0

#     def print(self):
#         self.s1.print()


class MyQueue(object):

    def __init__(self):
        self.s1 = MyStack() # 输入栈
        self.s2 = MyStack() # 输出栈

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.push(x)


    def pop(self):
        """
        :rtype: int
        """
        if self.s2.is_empty(): # 当且仅当输出栈为空时进行全部元素的转移
            while self.s1.size():
                self.s2.push(self.s1.pop())
        return self.s2.pop()


    def peek(self):
        """
        :rtype: int
        """
        temp = self.pop()
        self.s2.push(temp)
        return temp

    def empty(self):
        """
        :rtype: bool
        """
        return self.s1.size() == 0 and self.s2.size() == 0

    def print(self):
        self.s1.print()


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.print()
obj.push(2)
obj.print()
print(obj.peek())
obj.print()
print(obj.pop())
obj.print()
print(obj.empty())
obj.print()

"""
栈
设计
队列

需要两个栈：输入栈和输出栈
输入栈：进来新元素时直接压入该栈
输出栈：从该栈中出元素，以确定是队列的顺序

当输出栈为空时，出元素时需要将输入栈的所有元素移动至输出栈
不为空时直接从输出栈中出元素即可

"""
