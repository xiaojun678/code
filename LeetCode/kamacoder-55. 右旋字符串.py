k = int(input())
# Python字符串不可改
# 这里使用列表，即假设可以字符串可以改，从而实现O(1)空间复杂度
strs = list(input()) 

n = len(strs)
idx = n - k

while idx > 0:
    tmp = idx - k
    if tmp < 0:
        tmp = 0
    
    start1 = tmp
    start2 = idx
    while start1 < tmp + k:
        strs[start1], strs[start2] = strs[start2], strs[start1]

        start1 += 1
        start2 += 1
    
    idx = tmp

print(''.join(strs))

# O(1)空间的另一种做法是先整体反转，再分别对两段（前k字符、其余字符）分别做反转

"""
Python简便解法：
k = int(input())
strs = input()

print(strs[-k:]+strs[:-k])


"""