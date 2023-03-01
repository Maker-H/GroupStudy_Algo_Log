# BFS
from collections import deque

def bfs(x):
    q.append(x)
    visited[x] = 1
    _sum = []
    while q:
        y = q.popleft()
        _sum.append(cost[y])
        for j in friend[y]:
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)
    return _sum


N, M, K = map(int, input().split())
cost = [0] + list(map(int, input().split()))
friend = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
q = deque()
_set = []
for i in range(1, N+1):
    if visited[i] == 0:
        tmp = bfs(i)
        _set.append(tmp)


ans = 0
for s in _set:
    ans += min(s)


if ans > K:
    print('Oh no')
else:
    print(ans)

    
# UnionFind

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    # 친구비를 기준으로 부모 설정
    if cost[x] < cost[y]:
        parent[y] = x
    else:
        parent[x] = y


N, M, K = map(int, input().split())
cost = [0] + list(map(int, input().split()))
parent = [i for i in range(N + 1)]

# 친구 관계 구현
for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)
ans = 0
friend = set()
for i in range(1, N + 1):
    if find(i) not in friend:
        ans += cost[parent[i]]
        friend.add(parent[i])

if ans > K:
    print("Oh no")
else:
    print(ans)


