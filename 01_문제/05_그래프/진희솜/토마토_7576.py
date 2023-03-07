import sys
from collections import deque
# 익은 토마토 찾기
def find_tomato():
    for f in range(M):
        for s in range(N):
            if box[f][s] == 1:
                candids.append([f, s])

def bfs():
    Q = deque()
    max_date = 0

    for f, s in candids:
        Q.append([f, s, 0])

    while Q:
        f, s, cnt = Q.popleft()

        if cnt > max_date:
            max_date = cnt

        for k in range(4):
            nf = f + df[k]
            ns = s + ds[k]
            if 0 <= nf < M and 0 <= ns < N and box[nf][ns] == 0:
                box[nf][ns] = 1
                Q.append([nf, ns, cnt + 1])

    return max_date

df = [0, 0, 1, -1]
ds = [1, -1, 0, 0]

N, M = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# 모든 토마토가 익어 있으면 0 출력
not_ripe = False
for b in box:
    if 0 in b:
        not_ripe = True
        break

if not not_ripe:
    print(0)
else:
    # 익은 토마토 찾기
    candids = []
    find_tomato()

    # 가보자고
    total_date = bfs()

    # 토마토가 모두 익지 못하는 상황이면 -1 출력\
    not_ripe = False
    for b in box:
        if 0 in b:
            not_ripe = True
            break

    if not_ripe:
        print(-1)
    else:
        print(total_date)


