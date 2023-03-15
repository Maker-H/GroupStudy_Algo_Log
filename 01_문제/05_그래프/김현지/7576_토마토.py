from collections import deque

di = [1, 0, 0, -1]
dj = [0, -1, 1, 0]


def find_cnt():  # 토마토 익을 때 까지의 최소 날짜 찾기
    max_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:   # 안 익은 토마토 있으면
                return -1
            # 방문체크 리스트를 통해 최소 날짜 찾기
            max_cnt = max(max_cnt, visited[i][j])
    return max_cnt


def bfs():
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            # 상자 크기를 벗어나지 않고, 안 익은 토마토, 방문하지 않은 곳일 때
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                Q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                arr[nx][ny] = 1


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 토마토 상자
visited = [([0]*M) for _ in range(N)]  # 방문 체크
Q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:  # 익은 토마토 위치
            Q.append([i, j])  # Q에 위치 삽입
bfs()
print(find_cnt())
