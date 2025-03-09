n, m = map(int,input().strip().split()) # 矩阵的行数和列数

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().strip().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]

tmp = []

# ### 深度优先遍历
# def dfs(x, y):
#     if visited[x][y] == 1 or matrix[x][y] == 0:
#         return

#     visited[x][y] = 1

#     ## 访问上下左右四个方向
#     # 上
#     if x-1>=0:
#         dfs(x-1, y)
#     # 下
#     if x+1<n:
#         dfs(x+1,y)
#     # 左
#     if y-1>=0:
#         dfs(x,y-1)
#     # 右
#     if y+1<m:
#         dfs(x, y+1)

### 广度优先遍历
def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = 1 # 加入队列时就代表走过 避免重复加入
    while len(queue):
        x, y = queue.pop(0)
        # 上
        if x-1>=0 and matrix[x-1][y] == 1 and visited[x-1][y] == 0:
            queue.append((x-1, y))
            visited[x-1][y] = 1
        # 下
        if x+1<n and matrix[x+1][y] == 1 and visited[x+1][y] == 0:
            queue.append((x+1, y))
            visited[x+1][y] = 1
        # 左
        if y-1>=0 and matrix[x][y-1] == 1 and visited[x][y-1] == 0:
            queue.append((x, y-1))
            visited[x][y-1] = 1
        # 右
        if y+1<m and matrix[x][y+1] == 1 and visited[x][y+1] == 0:
            queue.append((x, y+1))
            visited[x][y+1] = 1 

# 依次从每个点开始遍历
for i in range(n):
    for j in range(m):
        # 访问新陆地
        if visited[i][j] == 0 and matrix[i][j] == 1:
            tmp.append((i, j))
            bfs(i, j) # dfs(i,j)
print(len(tmp))






