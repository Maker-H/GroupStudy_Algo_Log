import sys
from collections import deque

df = [0, 0, 1, -1]
ds = [1, -1, 0, 0]

def bfs(f, s):
    Q = deque()
    Q.append([f, s, 0])
    # 시작할때
    visited[f][s][0] = 1
    while Q:
        f, s, break_wall = Q.popleft()

        if f == N - 1 and s == M - 1:
            return visited[f][s][break_wall]

        for k in range(4):
            nf = f + df[k]
            ns = s + ds[k]
            if 0 <= nf < N and 0 <= ns < M:
                # 갈 곳이 벽으로 안막혀 있는 경우 그리고 이전에 방문하지 않은 경우
                if maze[nf][ns] == 0 and visited[nf][ns][break_wall] == 0:
                    visited[nf][ns][break_wall] = visited[f][s][break_wall] + 1
                    # 이전의 벽 부딪힘을 상속
                    Q.append([nf, ns, break_wall])

                # 갈 곳이 벽으로 막혀 있는 경우 이전에 벽에 부딪힌 적 있는지 체크
                elif maze[nf][ns] == 1 and break_wall == 0:
                    visited[nf][ns][1] = visited[f][s][break_wall] + 1
                    # 부딪히든 부딪히지 않았던 이번에 부딪혔음으로 벽에 무조건 부딪혔음
                    Q.append([nf, ns, 1])

    return -1

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# cnt 대신 사용
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

cnt = bfs(0, 0)

print(cnt)