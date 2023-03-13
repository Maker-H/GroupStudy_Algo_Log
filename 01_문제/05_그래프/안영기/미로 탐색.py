# https://www.acmicpc.net/problem/2178
# [안영기] bfs / 미로탐색 / 실버

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(i, j):
    Q = []
    Q.append((i, j))
    visited[i][j] += 1

    while Q:
        si, sj = Q.pop(0)
        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[si][sj] + 1
                Q.append((ni, nj))



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
bfs(0, 0)
print(visited[N-1][M-1])
