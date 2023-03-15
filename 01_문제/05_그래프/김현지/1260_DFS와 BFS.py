from collections import deque


def dfs(v):
    visited_d[v] = 1
    print(v, end=' ')
    for w in range(1, N+1):
        if adj_mat[v][w] == 1 and visited_d[w] == 0:
            dfs(w)


def bfs(v):
    Q = deque()
    Q.append(v)
    visited_b[v] = 1

    while Q:
        v = Q.popleft()
        print(v, end=' ')
        for w in range(N+1):
            if adj_mat[v][w] == 1 and visited_b[w] == 0:
                Q.append(w)
                visited_b[w] = 1


N, M, V = map(int, input().split())
adj_mat = [[0]*(N+1) for _ in range(N+1)]  # 인접행렬리스트
visited_b = [0] * (N+1)  # bfs 방문체크
visited_d = [0] * (N+1)  # dfs 방문체크
for _ in range(M):
    a, b = map(int, input().split())
    adj_mat[a][b] = adj_mat[b][a] = 1

dfs(V)
print()
bfs(V)