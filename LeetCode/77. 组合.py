class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        ### 回溯法
        def backtracking(r, x):
            if len(r) == k: # 终止条件
                res.append(r[:]) # 浅拷贝
                return
            # 剪枝
            # 如果for循环选择的起始位置之后的元素个数已经不足需要的元素个数 则没有必要进行搜索
            for i in range(x+1, n+1):
                if n+1-i<k-len(r): # 剪枝
                    break
                r.append(i) # 处理节点
                backtracking(r, i) # 递归
                r.pop() # 回溯，撤销处理结果
        backtracking([], 0)
        return res


s = Solution()
print(s.combine(4, 2))





"""
回溯



回溯法模板：
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
必要时需要剪枝以加快速度



"""
