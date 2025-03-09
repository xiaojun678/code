class MinStack:

    def __init__(self):
        # 正常栈
        self.stack = []
        # 递减栈——方便快速获取最小值
        self.down_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.down_stack or self.down_stack[-1]>= val:
            self.down_stack.append(val)
        
    def pop(self) -> None:
        tmp = self.stack.pop()

        if self.down_stack[-1] == tmp:
            self.down_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.down_stack[-1] # 永远不会为空

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



"""
栈
设计

"""