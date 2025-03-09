class Solution:
    def permute(self, nums):
        res = []
        path = []

        def digui(path, start):
            if len(path) == len(nums):
                res.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                nums[start], nums[i] = nums[i], nums[start] # 交换顺序 避免一个数被多次加入

                digui(path, start+1)

                path.pop()
                nums[start], nums[i] = nums[i], nums[start]

        digui(path, 0)
        return res



"""
数组
回溯


"""