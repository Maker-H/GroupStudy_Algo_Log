from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    flag = 0
    visited[x] = 1
    while q:
        i = q.popleft()
        if flag == 0 and len(tree[i]) > 2:
            # 간선의 수가 2개 이상일때 기둥이 아님
            # print(i)
            ans = visited[i]-1
            flag = 1
        if flag == 0 and len(tree[i]) > 1 and i == x: 
            # 주의 루트 노드일 때는 간선의 수가 2개이상이면 기둥이 아님
            ans = 0
            flag = 1
        for j, k in tree[i]:
            if visited[j] == 0:
                visited[j] = visited[i] + k # 거리 갱신
                q.append(j)
    if flag == 1: # 가지가 있을 때
        return ans, max(visited) - 1 - ans
    else: # 가지가 없을 때
        return max(visited)-1, 0

N, root = map(int, input().split())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])
visited = [0]*(N+1)
i = root
a = bfs(i)
print(*a)


