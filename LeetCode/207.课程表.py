class Solution(object):
    ### 拓扑排序判断有向图中是否存在环
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 入度
        inDegree = [0]*numCourses
        # 邻接表
        matrix = [[] for _ in range(numCourses)]
        # 初始化入度和邻接矩阵
        for p in prerequisites:
            matrix[p[0]].append(p[1])
            inDegree[p[1]] += 1
        
        count = 0
        queue = []
        # 先加入入度为0的节点
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)
        
        while queue:
            # 依次从图中删除入度为0的节点
            p = queue.pop(0) # 确保先进先出
            count += 1
            # 被删除节点指向的节点
            for node in matrix[p]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    queue.append(node)
        # 节点能全部删除代表无环
        return count == numCourses

    ### 深度优先遍历
    def canFinish(self, numCourses, prerequisites):
        """
        https://leetcode.cn/problems/course-schedule/solutions/18806/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
        """
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True # 当 flag[i] == -1，说明当前访问节点已被其他节点启动的 DFS 访问，无需再重复搜索
            if flags[i] == 1: return False # 当 flag[i] == 1，说明在本轮 DFS 搜索中节点 i 被第 2 次访问，即 课程安排图有环
            # 当前正在访问
            flags[i] = 1
            for j in adjacency[i]: 
                # 深度访问下一个节点
                if not dfs(j, adjacency, flags): 
                    return False 
            # 当前节点被访问完毕
            flags[i] = -1
            return True

        # 邻接表
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        
        # flags判断节点i的状态（三个）：0 -1 1
        flags = [0 for _ in range(numCourses)]
        
        # 对每个节点依次进行dfs
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True



"""
深度优先搜索
广度优先搜索
图
拓扑排序



"""


