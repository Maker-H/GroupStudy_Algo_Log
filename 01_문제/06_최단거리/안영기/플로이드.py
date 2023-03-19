# https://www.acmicpc.net/problem/11404
# [안영기] 플로이드-워셜 / 플로이드 / 골드

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = 10**10
cost = [[inf]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a - 1][b - 1] = min(cost[a-1][b-1], c) # 노선 중 최소값 입력


for k in range(n):
    for i in range(n):
        for j in range(n):
            if not i == j:
                # 직접 가는 노선, 경로를 거치는 노선 중 최소값 입력
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# 경로가 없으면 0으로 출력
for i in range(n):
    for j in range(n):
        if cost[i][j] == inf:
            cost[i][j] = 0

for lst in cost:
    print(*lst)


