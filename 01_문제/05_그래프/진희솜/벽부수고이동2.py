import sys
from collections import deque

df = [0, 0, 1, -1]
ds = [1, -1, 0, 0]

def bfs(f, s):
    Q = deque()
    Q.append([f, s, 0])
    # 시작하는 칸도 포함해서 센다
    visited[f][s][0] = 1
    min_cnt = M * N * K + 3
    is_ended = False
    while Q:
        f, s, break_wall = Q.popleft()

        # 가지치기
        if break_wall > K:
            continue
        if visited[f][s][break_wall] > min_cnt:
            continue

        if f == N - 1 and s == M - 1:
            return visited[f][s][break_wall]

        for k in range(4):
            nf = f + df[k]
            ns = s + ds[k]

            if 0 <= nf < N and 0 <= ns < M:
                # 갈 곳의 벽이 없다면
                if maze[nf][ns] == 0 and break_wall <= K and visited[nf][ns][break_wall] == 0:
                    Q.append([nf, ns, break_wall])
                    visited[nf][ns][break_wall] = visited[f][s][break_wall] + 1

                # 벽을 이미 k번 부쉈다면 더 부수지 못한다
                elif maze[nf][ns] == 1 and break_wall < K and visited[nf][ns][break_wall + 1] == 0:
                    visited[nf][ns][break_wall + 1] = visited[f][s][break_wall] + 1
                    Q.append([nf, ns, break_wall + 1])

    return -1

N, M, K = map(int, sys.stdin.readline().split())

maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# K개 까지 부숴도 되는거라서 K + 1로 visited 만들어준다
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]

cnt = bfs(0, 0)
print(cnt)