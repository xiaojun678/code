class Solution:
    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            # 和最右边的数进行比较
            if nums[pivot] <= nums[high]: # low和high不相等 所以pivot不存在等于high的情况
                high = pivot 
            else:
                low = pivot + 1
        return nums[low]

"""
疑问：为什么while的条件是low<high,而不是low<=high呢
解答：low<high，假如最后循环到{*,10,1,*}的这种情况时，nums[low]=10,nums[high]=1,nums[mid]=10,low=mid+1,
    直接可以跳出循环了,所以low<high,此时low指向的就是最小值的下标;
    如果low<=high的话，low=high，还会再不必要的循环一次，此时最后一次循环的时候会发生low==high==mid，
    则nums[mid]==nums[high]，则会走一次else语句，则low=mid+1,此时low指向的是最小值的下一个下标，
    则需要return[low-1]

"""



"""
数组
二分查找


"""


            







        