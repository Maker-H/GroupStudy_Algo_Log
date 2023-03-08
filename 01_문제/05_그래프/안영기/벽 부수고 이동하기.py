# https://www.acmicpc.net/problem/2206
# [안영기] bfs / 벽부수고이동하기 / 골드
from collections import deque

def bfs():
    Q = deque()
    Q.append((0, 0, 0))
    visited[0][0][0] = 1
    while Q:
        si, sj, z = Q.popleft()
        if si == N-1 and sj == M-1:
            return visited[si][sj][z]
        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            # 벽을 만났고 파괴할 수 있는 경우 카운팅, 이동
            if arr[ni][nj] == 1 and z == 0:
                visited[ni][nj][1] = visited[si][sj][0] + 1
                Q.append((ni, nj, 1))
            # 벽이 아닌 길이고 방문하지 않은 경우
            elif arr[ni][nj] == 0 and visited[ni][nj][z] == 0:
                visited[ni][nj][z] = visited[si][sj][z] + 1
                Q.append((ni, nj, z))

    return -1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# 3차원으로 배열을 만들어 벽 파괴 기회를 쓴 경우, 안쓴 경우를 따로 진행
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
print(bfs())
