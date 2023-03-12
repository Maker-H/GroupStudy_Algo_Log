from collections import deque
import sys; input = sys.stdin.readline
# 토마토 상자가 3차원이므로 x, y, z가 필요
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while q:
        x, y, z = q.popleft()
        for r in range(6):
            nx, ny, nz = x + dx[r], y + dy[r], z+ dz[r]
            if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                if arr[nx][ny][nz] == 0:
                    q.append((nx,ny,nz))
                    # 시간을 알아야 하므로 + 1 해줌
                    arr[nx][ny][nz] = arr[x][y][z] + 1

def check():
    _max = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return -1
                else:
                    # 최댓값 확인
                    if _max < arr[i][j][k]:
                        _max = arr[i][j][k]

    return _max - 1


M, N, H = map(int,input().split())
arr = []
q = deque()
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, input().split())))
    for j in range(N):
        for k in range(M):
            if tmp[j][k] == 1:
                q.append((i, j, k))
    arr.append(tmp)
    
bfs()
print(check())