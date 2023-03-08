# https://www.acmicpc.net/problem/7576
# [안영기] bfs / 토마토 / 골드
git commit -m '[안영기] bfs / 토마토 / 골드' -m 'https://www.acmicpc.net/problem/7576'
import sys
from collections import deque
inpupt = sys.stdin.readline

def find_ans():
    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:      # 덜 익은 토마토가 있으면
                return -1           # 실패
            if arr[i][j] >= ans:
                ans = arr[i][j]
    return ans - 1

# 4방향 탐색
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# bfs
Q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:      # 익은 토마토 모두 저장
            Q.append((i, j))

while Q:
    si, sj = Q.popleft()
    for k in range(4):
        ni, nj = si + di[k], sj + dj[k]
        if 0<=ni<N and 0<=nj<M:
            if arr[ni][nj] == 0:    # 익은 토마토 4방향에 덜익은 토마토가 있으면
                arr[ni][nj] = arr[si][sj] + 1   # +1 한 후 저장
                Q.append((ni, nj))

print(find_ans())








