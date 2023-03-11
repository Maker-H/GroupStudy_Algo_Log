from collections import deque

di = [1, 0, 0, -1]
dj = [0, -1, 1, 0]

def bfs(x, y):
    Q = deque()
    Q.append([x,y])
    visited[x][y] = 1
    while Q:
        x, y = Q.popleft()
        if x == N-1 and y == M-1:  # (N, M)위치에 도착하면
            return visited[x][y]
        else:
            for i in range(4):
                nx = x + di[i]
                ny = y + dj[i]
                # 미로 크기를 벗어나지 않고, 벽이 아닌, 방문하지 않은 곳일 때
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    Q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [([0]*M) for _ in range(N)]

print(bfs(0,0))
