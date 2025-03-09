strs = input()
n = len(strs)
res = ''

for i in range(n):
    if '0' <= strs[i] <= '9':
        res += 'number'
    else:
        res += strs[i]

print(res)

"""
O(n)空间做法：
扩充旧数组的大小为新数组大小，从后向前替换：
双指针-右指针指向新数组末尾，左指针指向旧数组末尾
两指针从后向前，左指针的值依次赋给右指针（数值赋为number）
"""