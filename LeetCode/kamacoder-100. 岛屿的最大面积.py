n, m = map(int, input().strip().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().strip().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]
max_area = 0

### 深搜法
def dfs(x, y, area):
    if matrix[x][y] == 0 or visited[x][y] == 1:
        return area
    
    visited[x][y] = 1
    area += 1
    # 上下左右
    if x-1>=0:
        area = dfs(x-1, y, area)
    if x+1<n:
        area = dfs(x+1, y, area)
    if y-1>=0:
        area = dfs(x, y-1, area)
    if y+1<m:
        area = dfs(x, y+1, area)
    return area

### 广搜法
def bfs(x, y, area):
    queue = [(x, y)]
    visited[x][y] = 1
    area += 1
    while len(queue):
        x, y = queue.pop(0)

        if x-1>=0 and matrix[x-1][y] == 1 and visited[x-1][y] == 0:
            queue.append((x-1, y))
            visited[x-1][y] = 1
            area += 1

        if x+1<n and matrix[x+1][y] == 1 and visited[x+1][y] == 0:
            queue.append((x+1, y))
            visited[x+1][y] = 1
            area += 1

        if y-1>=0 and matrix[x][y-1] == 1 and visited[x][y-1] == 0:
            queue.append((x, y-1))
            visited[x][y-1] = 1
            area += 1

        if y+1<m and matrix[x][y+1] == 1 and visited[x][y+1] == 0:
            queue.append((x, y+1))
            visited[x][y+1] = 1
            area += 1
    
    return area


for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            # a = dfs(i, j, 0)
            a = bfs(i, j, 0)
            max_area = a if a > max_area else max_area
print(max_area)




