import sys
from collections import deque


di = [1,-1,0,0,0,0]
dj = [0,0,1,-1,0,0]
dz = [0,0,0,0,-1,1]

def find_(arr):                     # 토마토 찾기
    for z in range(H):
        for i in range(M):
            for j in range(N):

                if arr[z][i][j] == 1:
                    Q.append([z,i,j])

def bfs(Q):

    while Q:
        z,i,j = Q.popleft()
        for s in range(6):
            ni = i + di[s]
            nj = j + dj[s]
            nz = z + dz[s]

            if 0 <= ni < M and 0 <= nj < N and 0 <= nz < H: # 익지않은 토마토에 값 넣어줌
                if arr[nz][ni][nj] == 0:
                    arr[nz][ni][nj] = arr[z][i][j] + 1
                    Q.append([nz, ni, nj])





N,M,H = map(int,sys.stdin.readline().split())
arr = [[list(map(int,sys.stdin.readline().split())) for _ in range(M)] for _ in range(H)]       # 3차원배열 생성


Q=deque()
find_(arr)
bfs(Q)
flag = 0

max_ = -2
for z in range(H):
    for i in range(M):
        for j in range(N):
            if arr[z][i][j] == 0:           # 익지 않은 토마토값있으면 flag = 1
                flag = 1

            max_ = max(max_,arr[z][i][j])   # 날짜 세기

if flag == 1:
    print(-1)

elif max_ == -1:
    print(0)

else:
    print(max_ - 1)



