import sys
from collections import deque


di = [1,-1,0,0]
dj = [0,0,1,-1]

def find_(arr):                     # 토마토 위치 찾기
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                Q.append([i,j])     # Q에 넣기

def bfs(Q):

    while Q:
        i,j = Q.popleft()
        for s in range(4):          # 4 방향탐색
            ni = i + di[s]
            nj = j + dj[s]

            if 0 <= ni < M and 0 <= nj < N:
                if arr[ni][nj] == 0:        # 익지않은 토마토에 값넣어줌
                    arr[ni][nj] = arr[i][j] + 1
                    Q.append([ni, nj])





N,M = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]


Q=deque()
find_(arr)
bfs(Q)
flag = 0

max_ = 0
for s in arr:               # flag로 익지않은토마토가 있으면 -1 출력
    for k in s:
        if k == 0:
            flag = 1

    max_ = max(max_,max(s))

if flag == 0:
    print(max_ -1)
else:
    print(-1)



