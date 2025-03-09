class Solution(object):
    """
    本题核心思路：每个数字可以接的雨水量取决于两边最大值的较小者
    """
    ### 动态规划法
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 每个数字可以接的雨水量取决于两边最大值的较小者
        n = len(height)
        leftMax = [height[0]] + [0]*(n-1)
        rightMax = [0]*(n-1) + [height[n-1]]
        # 分别把每个数字的两边最大值求解出来（包含自身）
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1], height[i])
        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1], height[i])
        # 每个值可接的雨水
        ans = [min(leftMax[i],rightMax[i])-height[i] for i in range(n)]

        return sum(ans)

    ### 单调栈法
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        # 存放下标 从底到上递减
        stack = []
        for i in range(len(height)):
            while len(stack) and height[i]>height[stack[-1]]:
                temp = stack.pop()
                if len(stack):
                    x = height[i] if height[i]<height[stack[-1]] else height[stack[-1]]
                    area += (x - height[temp])*(i-stack[-1]-1) # 当前下标减去栈顶第一个元素
            stack.append(i)
            
        return area

    ### 双指针法——改进动态规划中的leftMax和rightMax数组
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n-1

        leftMax = 0
        rightMax = 0

        ans = 0

        while left<right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            # 看下方解释
            if leftMax < rightMax:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))




"""
栈
数组
双指针
动态规划
单调栈

存在动态规划、双指针和单调栈三种解法


// 双指针解法
// 注意到动态规划中
// 对于位置 i 的接水量取决于 leftMax 和 rightMax 中的较小者
// 所以我们不必真的知道较大者是谁
// 只要知道较小者是谁就可以了 

假设两柱子分别为 i，j。那么就有 iLeftMax,iRightMax,jLeftMx,jRightMax 这个变量。由于 j>i ，
故 jLeftMax>=iLeftMax，iRigthMax>=jRightMax.

那么，如果 iLeftMax>jRightMax，则必有 jLeftMax >= jRightMax，所有我们能接 j 点的水。
如果 jRightMax>iLeftMax，则必有 iRightMax >= iLeftMax，所以我们能接 i 点的水。
而上面我们实际上只用到了 iLeftMax，jRightMax 两个变量，故我们维护这两个即可。

// 初始化 left = 0, right = n-1, leftMax = 0, rightMax = 0
// 注意到对于位置 left 来说, leftMax 是真正意义上的左侧最大值, 而 rightMax 不是真的右侧最大值
// 而对于位置 right 来说, rightMax 是真正意义上的右侧最大值, 而 leftMax 不是真的左侧最大值

"""