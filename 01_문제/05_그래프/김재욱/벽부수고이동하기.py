from collections import deque
from copy import deepcopy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][z]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    q.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                # 벽을 부술 수 있으면 벽을 부숨
                elif arr[nx][ny] == 1 and z == 0:
                    q.append((nx,ny,z+1))
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
    return -1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
q = deque()
# 벽을 부수고 이동하였을 때 visited가 달라야 하므로 3차원으로 만듬
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(bfs())
