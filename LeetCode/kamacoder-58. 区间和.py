# 数组长度
n = int(input())
# 数组元素
nums = [0]*n
for i in range(n):
    nums[i] = int(input())
# 前缀和
sums = [0]
for i in range(n):
    sums.append(nums[i]+sums[-1])

# 不指定用例数量的处理方式
while 1:
    try:
        start, end = map(int, input().split())
        print(sums[end+1]-sums[start])
    except:
        break


"""
前缀和

"""