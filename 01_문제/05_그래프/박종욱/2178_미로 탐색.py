
di = [-1,0,0,1]
dj = [0,-1,1,0]

def bfs(i,j):
    Q = []
    Q.append((i,j))
    visited[i][j] = 1           # 방문체크
    while Q:
        i,j = Q.pop(0)
        for s in range(4):
            ni = i + di[s]
            nj = j + dj[s]
            if 0 <= ni < N+1 and 0 <= nj < M+1:
                if arr[ni][nj] == 1:
                    if not visited[ni][nj]:
                        Q.append((ni,nj))
                        visited[ni][nj] = visited[i][j] + 1 # 방문체크
                elif ni == N and nj == M:           # 도착점일때 return
                    return




N,M = map(int,input().split())
arr = [[0]*(M+1)] + [[0]+ list(map(int,input())) for _ in range(N)]
visited = [[0]*(M+1) for _ in range(N+1)]

i = 1
j = 1
bfs(i,j)

print(visited[N][M])