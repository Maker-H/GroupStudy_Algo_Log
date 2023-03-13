# https://www.acmicpc.net/problem/7569
# [안영기] bfs / 토마토 / 골드
import sys
from collections import deque
inpupt = sys.stdin.readline

def find_ans():
    ans = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:           # 0이 있으면 -1 출력
                    return -1
                if arr[i][j][k] > ans:
                    ans = arr[i][j][k]
    return ans - 1      # 모든 배열을 돌았을 때 0이 없으면 최대값 -1 출력

di = [-1,1,0,0,0,0]     # 위 아래 상 하 좌 우
dj = [0,0,-1,1,0,0]
dk = [0,0,0,0,-1,1]

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]       # 리스트를 한겹 더 싸서 3차원 배열로 만들기

Q = deque()
for i in range(H):          # 층
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                Q.append((i,j,k))

while Q:
    si, sj, sk = Q.popleft()
    for l in range(6):
        ni = si + di[l]
        nj = sj + dj[l]
        nk = sk + dk[l]
        if 0<=ni<H and 0<=nj<N and 0<=nk<M:
            if arr[ni][nj][nk] == 0:
                arr[ni][nj][nk] = arr[si][sj][sk] + 1
                Q.append((ni, nj, nk))

print(find_ans())




