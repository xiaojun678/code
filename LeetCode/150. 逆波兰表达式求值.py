class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        flags = ['+', '-', '*', '/']
        for token in tokens:
            if token not in flags:
                stack.append(int(token))
            else:
                t1 = stack.pop()
                t2 = stack.pop()

                if token == '+':
                    stack.append(t2 + t1)
                elif token == '-':
                    stack.append(t2 - t1)
                elif token == '*':
                    stack.append(t2 * t1)
                else:
                    """
                    python的b/a会向下取整， 比如 -1 / 132 = -1。 题目要求是取整数部分，那么负数的时候，实际应该是向上取整， 解决方法： int(b / float(a))

                    python3 b/a会转为小数计算，所以直接 int(b/a)， 不能 b//a
                    """
                    stack.append(int(t2 / t1))
        
        return stack[-1]
    
s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

"""
栈
数组
数学


"""


