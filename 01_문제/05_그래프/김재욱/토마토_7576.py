di = [1,0,-1,0]
dj = [0,-1,0,1]
def bfs():
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and tomato[ni][nj] == 0:
                q.append((ni,nj))
                # 시간을 알아야 하므로 + 1 해줌
                tomato[ni][nj] = tomato[i][j] + 1

from collections import deque
q = deque()
M, N = map(int,input().split())

tomato = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j))
bfs()
flag = 1
_max = 0
for i in range(N):
    for j in range(M):
        # 익지 않은 토마토 있는지 확인
        if tomato[i][j] == 0:
            flag = 0
            break
        # 모두 익었으면 걸렸는시간 확인
        elif _max < tomato[i][j]:
            _max = tomato[i][j]
if flag == 1:
    print(_max-1)
else:
    print(-1)
