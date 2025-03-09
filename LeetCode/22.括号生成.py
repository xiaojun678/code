class Solution:
    def generateParenthesis(self, n: int):
        res = []
        path = ''

        def digui(path, num):
            if len(path) == n*2:
                res.append(path)
                return
            
            x1 = num # (数量
            x2 = len(path)-num # )数量

            if x1 < n: # 可以填左括号
                path += '('
                digui(path, x1+1)
                path = path[:-1]
            if x2 < x1: # 可以填右括号
                path += ')'
                digui(path, x1)
                path = path[:-1]
        

        digui(path, 0)
        return res


"""
字符串
动态规划
回溯

"""