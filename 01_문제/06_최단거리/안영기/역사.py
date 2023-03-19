# https://www.acmicpc.net/problem/1613
# [안영기] 플로이드-워셜 / 역사 / 골드

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
evt = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    evt[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if evt[i][k] + evt[k][j] == 2:
                evt[i][j] = 1

s = int(input())
for _ in range(s):
    x, y = map(int, input().split())
    if evt[x-1][y-1] == 1:
        print(-1)
    elif evt[y-1][x-1] == 1:
        print(1)
    else:
        print(0)

