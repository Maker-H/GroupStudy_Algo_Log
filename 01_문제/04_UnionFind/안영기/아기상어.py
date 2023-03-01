# https://www.acmicpc.net/problem/16236
# [안영기] 그래프 탐색 / 아기상어 / 골드

import sys
from collections import deque
input = sys.stdin.readline

def find_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return i, j


def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited = [[0]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    can_eat = []

    visited[x][y] = 1       # 방문체크

    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                if shark_size >= arr[ni][nj]:   # 상어보다 크지 않으면 이동 가능
                    Q.append([ni, nj])          # 이동하면서 방문체크, 거리 카운트
                    visited[ni][nj] = 1
                    distance[ni][nj] = distance[i][j] + 1

                    # 이동 가능 한 곳이 상어보다 작으면 리스트에 추가
                    if arr[ni][nj] < shark_size and arr[ni][nj] != 0:
                        can_eat.append([ni, nj, distance[ni][nj]])

    # 거리가 가까운 것을 우선, 같으면 가장 위, 또 같으면 왼쪽부터
    can_eat.sort(key = lambda x : (x[2], x[0], x[1]))
    return can_eat



# 이동방향
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
shark_size = 2
shark_eat = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

idx, jdx = find_shark()

cnt = 0
while True:
    fish_lst = bfs(idx, jdx)

    if len(fish_lst) == 0:  # 먹을 수 있는 물고기가 더 이상 없으면 종료
        print(cnt)
        break

    # bfs 결과를 오름차순으로 출력해서 가장 가까운 먹이가 첫번째 인덱스에 오게 됨
    idx, jdx, distance = fish_lst[0]


    shark_eat += 1
    if shark_size == shark_eat: # 자신의 크기만큼 물고기를 먹으면 레벨업
        shark_eat = 0
        shark_size += 1

    arr[idx][jdx] = 0   # 먹은 물고기는 사라짐
    cnt += distance



