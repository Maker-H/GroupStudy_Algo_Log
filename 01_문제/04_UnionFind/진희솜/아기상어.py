import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(f, s, shark_size):
    visited = [[-1] * N for _ in range(N)]
    Q = deque()
    candidate = []

    Q.append([f, s])
    visited[f][s] = 0

    while Q:
        f, s = Q.popleft()

        for k in range(4):
            nf = f + dx[k]
            ns = s + dy[k]
            if 0 <= nf < N and 0 <= ns < N and visited[nf][ns] == -1 and shark_food[nf][ns] <= shark_size:
                # 시간 얼마나 걸리는지 체크
                visited[nf][ns] = visited[f][s] + 1
                Q.append([nf, ns])

                # 상어 먹이가 0이 아니면 먹이 후보로 선정
                if shark_food[nf][ns] != 0 and shark_food[nf][ns] < shark_size:
                    candidate.append([nf, ns, shark_food[nf][ns], visited[nf][ns]])

    return candidate


N = int(sys.stdin.readline())
shark_food = []
for _ in range(N):
    shark_food.append(list(map(int, sys.stdin.readline().split())))

for f in range(N):
    for s in range(N):
        if shark_food[f][s] == 9:
            start_f, start_s = f, s
            break
    if shark_food[f][s] == 9:
        break

# 상어 있던 곳 0으로 바꿔준다
shark_food[start_f][start_s] = 0



candidate = bfs(start_f, start_s, 2)
shark_size = 2
total_time = 0
food_cnt = 0
while candidate:
    candidate = sorted(candidate, key=lambda x: (x[3], x[0], x[1]))

    mf, ms, food_size, moving_time = candidate[0]


    total_time += moving_time

    food_cnt += 1

    # 상어 크기 만큼 먹으면 크기 증가
    if food_cnt == shark_size:
        shark_size += 1
        food_cnt = 0
    
    shark_food[mf][ms] = 0
    candidate = bfs(mf, ms, shark_size)
    
print(total_time)

