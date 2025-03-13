class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        path = []

        candidates = list(sorted(candidates)) # 排序

        def digui(start, sums):
            if sums == target:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # 避免重复
                if i != start and candidates[i] == candidates[i-1]:
                    continue

                if sums + candidates[i] <= target:
                    path.append(candidates[i])
                    digui(i+1, sums + candidates[i])
                    path.pop()
                else:
                    break

        digui(0, 0)
        return res


"""
数组
回溯


"""