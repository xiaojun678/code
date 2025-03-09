class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        path = ''

        def digui(path, idx):
            if idx == len(digits):
                res.append(path)
                return
            
            num = int(digits[idx])
            for i in range((len(words[num-2]))):
                path += words[num-2][i]

                digui(path, idx+1)

                path = path[:-1]
            
        digui(path, 0)
        return res



"""
哈希表
字符串
回溯

"""