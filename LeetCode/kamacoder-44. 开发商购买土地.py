n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 每行前缀和
rows_sum = []
for i in range(n):
    if i != 0:
        temp = rows_sum[-1]
    else:
        temp = 0
    rows_sum.append(temp + sum(matrix[i]))
# 每列前缀和
cols_sum = []
for j in range(m):
    if j != 0:
        temp = cols_sum[-1]
    else:
        temp = 0
    cols_sum.append(temp + sum([matrix[i][j] for i in range(n)]))

ans = float('inf')
# 按行切分
for i in range(n-1):
    ans = min(ans, abs(rows_sum[-1]-2*rows_sum[i]))

# 按列切分
for j in range(m-1):
    ans = min(ans, abs(cols_sum[-1]-2*cols_sum[j]))

print(ans)








