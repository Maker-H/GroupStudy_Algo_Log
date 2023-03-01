# DFS

def dfs(v):
    visited[v] = 1
    for w in range(N):
        if graph[v][w] == 1 and visited[w] == 0:
            dfs(w)


N = int(input())
M = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split()))) # 연결되어있는 도시들을 그래프로 나타냄

route = list(map(int,input().split()))
visited = [0]*N
dfs(route[0] - 1) # 탐색을 통해 도시가 연결되어있는지 확인
flag = 1
for r in route:
    if visited[r-1] == 0:
        flag= 0
        break
if flag == 1:
    print('YES')
else:
    print('NO')

# UnionFind

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if parent[x] < parent[y]:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
M = int(input())
parent = [i for i in range(N)]
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        if tmp[j] == 1: # 연결되어있는 도시끼리 union
            union(i, j)

route = list(map(int,input().split()))
flag = 1
p = parent[route[0] - 1]
for r in route:
    if p != parent[r - 1]:
        flag = 0
        break
if flag == 1:
    print('YES')
else:
    print('NO')

