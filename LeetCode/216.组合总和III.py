class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res  = []
        ### 回溯法
        def backtracking(r, path, idx):
            if r == 0 and len(path) == k:
                res.append(path[:])
                return
            if len(path) == k:
                return
            
            for i in range(idx,10):
                num = k - len(path)
                if r < i*num: # 剪枝
                    break

                r = r - i
                path.append(i)

                backtracking(r, path, i+1)

                path.pop()
                r = r + i
        
        backtracking(n, [], 1)

        return res

s = Solution()
print(s.combinationSum3(3,7))



"""
数组
回溯


"""
