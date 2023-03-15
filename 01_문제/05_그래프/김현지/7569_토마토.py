from collections import deque

dh = [0, 0, 0, 0, 1, -1]
di = [1, 0, 0, -1, 0, 0]
dj = [0, -1, 1, 0, 0, 0]


def find_cnt():  # 토마토 익을 때 까지의 최소 날짜 찾기
    max_cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 0:
                    return -1
                # 방문체크 리스트를 통해 최소 날짜 찾기
                max_cnt = max(max_cnt, visited[h][i][j])
    return max_cnt

def bfs():
    while Q:
        h, x, y = Q.popleft()
        for k in range(6):
            nh = h + dh[k]
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and arr[nh][nx][ny] == 0 and visited[nh][nx][ny] == 0:
                Q.append([nh, nx, ny])
                visited[nh][nx][ny] = visited[h][x][y] + 1
                arr[nh][nx][ny] = 1


M, N, H = map(int, input().split())  # 가로, 세로, 높이
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[([0]*M) for _ in range(N)] for _ in range(H)]
Q = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                Q.append([h, i, j])

bfs()
print(find_cnt())
