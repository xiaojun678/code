# ACM模式

n, m = map(int, input().strip().split()) # 获取第一行

data = [[0 for i in range(n)] for j in range(n)] # 邻接矩阵

# 需要矩阵承接数据时
for i in range(m):
	t1, t2 = map(int, input().strip().split())
	data[t1-1][t2-1] = 1
	
res = []

# 深度遍历
def dfs(r):
	if r[-1] == n:
		res.append(r[:])
		return
	for i in range(0, n):
		if data[r[-1]-1][i]:
			r.append(i+1)
			dfs(r)
			r.pop()

dfs([1])

if len(res):
	for i in range(len(res)):
		for j in range(len(res[i])-1):
			print(res[i][j], end=' ')
		print(res[i][-1])
else:
	print(-1)
	