class Solution:
    def partition(self, s: str):
        res = []
        path = []
        n = len(s)
        def digui(start, path):
            if start == n:
                res.append(path[:])
                return

            for i in range(start+1, n+1):
                t = s[start: i]
                if t == t[::-1]:  # 判断是否回文
                    path.append(t)
                    digui(i, path)
                    path.pop()

        digui(0, path)


"""
字符串
动态规划
回溯


"""