from collections import deque


def bfs(v):
    Q = deque()
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.popleft()
        for w in adj_lst[v]:  # 인접
            if not visited[w]:  # 방문체크
                Q.append(w)
                visited[w] = 1
                pc[w] = v  # w:자식, v:부모


N = int(input())
adj_lst = {i:[] for i in range(1, N+1)}
visited = [0] * (N+1)  # 방문 체크
pc = [0] * (N+1)  # 부모-자식 리스트

for _ in range(N-1):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

bfs(1)
for i in range(2, N+1):  # 2번 노드부터 출력
    print(pc[i])


