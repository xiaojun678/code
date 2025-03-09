class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)==1:
            return intervals
        intervals = sorted(intervals)
        n = len(intervals)
        ### 需要额外空间
        # ans = []
        # if intervals[1][0]<=intervals[0][1]:
        #     ans.append([intervals[0][0], max(intervals[1][1], intervals[0][1])])
        # else:
        #     ans.append(intervals[0])
        #     ans.append(intervals[1])
        # intervals.pop(0)
        # intervals.pop(0)
        # while len(intervals):
        #     if intervals[0][0]<=ans[-1][1]:
        #         ans[-1] = [ans[-1][0], max(intervals[0][1], ans[-1][1])]
        #     else:
        #         ans.append(intervals[0])
        #     intervals.pop(0)
        # return ans

        ### 不需要额外空间 但是remove函数的时间复杂度是O(n)
        num = 0
        while num <len(intervals)-1:
            # 需要合并
            if intervals[num+1][0]<=intervals[num][1]:
                intervals[num] = [intervals[num][0], max(intervals[num][1], intervals[num+1][1])]
                intervals.remove(intervals[num+1])
            # 不需要合并
            else:
                num += 1

        return intervals


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))


"""
数组
排序




"""