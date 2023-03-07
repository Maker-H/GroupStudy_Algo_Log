import sys
from collections import deque

df = [0, 0, 1, -1]
ds = [1, -1, 0, 0]


def bfs(f, s):
    Q = deque()
    global min_cnt
    global visited

    Q.append([0, 0, 1])
    visited[0][0] = 1
    while Q:
        f, s, cnt = Q.popleft()


        if f == N - 1 and s == M - 1:
            if min_cnt > cnt:
                min_cnt = cnt

        for k in range(4):
            nf = f + df[k]
            ns = s + ds[k]

            if 0 <= nf < N and 0 <= ns < M and visited[nf][ns] == 0 and maze[nf][ns] == '1':
                visited[nf][ns] = 1
                Q.append([nf, ns, cnt + 1])



N, M = map(int, sys.stdin.readline().split())

maze = [list(sys.stdin.readline()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
min_cnt = 100 * 100

bfs(0, 0)
print(min_cnt)