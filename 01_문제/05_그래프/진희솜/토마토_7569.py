from collections import deque
import sys

def find_tomato():
    for h in range(H):
        for f in range(N):
            for s in range(M):
                if boxes[h][f][s] == 1:
                    candids.append([h, f, s])

def is_all_ripe():
    for h in range(H):
        for f in range(N):
            for s in range(M):
                if boxes[h][f][s] == 0:
                    return False
    return True

def bfs():
    result_date = 0
    Q = deque()
    for h, f, s in candids:
        Q.append([h, f, s, 0])

    while Q:
        h, f, s, date = Q.popleft()

        if result_date < date:
            result_date = date

        for k in range(6):
            nf = f + df[k]
            ns = s + ds[k]
            nh = h + dh[k]
            if 0 <= nf < N and 0 <= ns < M and 0 <= nh < H and boxes[nh][nf][ns] == 0:
                boxes[nh][nf][ns] = 1
                Q.append([nh, nf, ns, date + 1])

    return result_date



df = [0, 0, 1, -1, 0, 0]
ds = [1, -1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]



M, N, H = map(int, sys.stdin.readline().split())

boxes = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for i in range(H)]

# 다 익어있는지 확인
if is_all_ripe():
    print(0)
else:
    # 익어있는 토마토
    candids = []
    find_tomato()
    cnt = bfs()

    # 시간 지난 후 다 익었는지 확인
    if is_all_ripe():
        print(cnt)
    else:
        print(-1)


