# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    ### 归并排序递归法：自顶向下 额外需要O(logn)的调用栈空间
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def sort(left):
            if not left or not left.next:
                return left

            # 从中间拆分
            fast = left
            slow = left
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            mid = pre
            temp = mid.next
            mid.next = None

            # 递归排序左边和右边
            l = sort(left)
            r = sort(temp)
            
            # 合并
            bin_head = ListNode()
            p = bin_head
            p1 = l
            p2 = r

            while p1 or p2:
                if p1 and p2:
                    if p1.val <= p2.val:
                        p.next = p1
                        p1 = p1.next
                    else:
                        p.next = p2
                        p2 = p2.next
                elif p1:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                
                p = p.next # 注意这个
            
            return bin_head.next

        return sort(head)
    
    ### 归并排序迭代法：从底至顶直接合并——待理解
    def sortList(self, head):
        h, length, intv = head, 0, 1
        while h: 
            h, length = h.next, length + 1
        # 虚拟头结点
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: 
                    h, i = h.next, i - 1
                if i: 
                    break # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: 
                    h, i = h.next, i - 1
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: 
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: 
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: 
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h 
            intv *= 2
        return res.next




ls = [5,3]

head = ListNode(ls[0])
p = head

for i in range(1, len(ls)):
    p.next = ListNode(ls[i])
    p = p.next

s = Solution()
s.sortList(head)



"""
链表
双指针
分治
排序
归并排序


归并排序有递归和迭代两种做法
对于迭代做法：
模拟上述的多轮排序合并：
    1.统计链表长度 length，用于通过判断 intv < length 判定是否完成排序；
    2.额外声明一个节点 res，作为头部后面接整个链表，用于：
        2.1 intv *= 2 即切换到下一轮合并时，可通过 res.next 找到链表头部 h；
        2.2 执行排序合并时，需要一个辅助节点作为头部，而 res 则作为链表头部排序合并时的辅助头部 pre；后面的合并排序可以将上次合并排序的尾部 tail 用做辅助节点。
    3.在每轮 intv 下的合并流程：
        3.1 根据 intv 找到合并单元 1 和单元 2 的头部 h1, h2。由于链表长度可能不是 2^n，需要考虑边界条件：
            3.1.1 在找 h2 过程中，如果链表剩余元素个数少于 intv，则无需合并环节，直接 break，执行下一轮合并；
            3.1.2 若 h2 存在，但以 h2 为头部的剩余元素个数少于 intv，也执行合并环节，h2 单元的长度为 c2 = intv - i。
        3.2 合并长度为 c1, c2 的 h1, h2 链表，其中：
            3.2.1 合并完后，需要修改新的合并单元的尾部 pre 指针指向下一个合并单元头部 h。（在寻找 h1, h2 环节中，h指针已经被移动到下一个单元头部）
            3.2.2 合并单元尾部同时也作为下次合并的辅助头部 pre。
        3.3 当 h == None，代表此轮 intv 合并完成，跳出。
    4.每轮合并完成后将单元长度×2，切换到下轮合并：intv *= 2

作者：Krahets
链接：https://leetcode.cn/problems/sort-list/solutions/13728/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

