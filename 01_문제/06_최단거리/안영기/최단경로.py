# https://www.acmicpc.net/problem/1753
# [안영기] 다익스트라 / 최단경로 / 골드

import sys
import heapq
input = sys.stdin.readline

def dijkstra(E):
    Q = []
    heapq.heappush(Q, (0, E))
    dist[E] = 0
    while Q:
        d, s = heapq.heappop(Q)
        for i in arr[s]:
            now = d + i[1]          # 현재 거리에 인접리스트 내의 가중치를 가산
            if now < dist[i[0]]:    # 최단거리면 갱신
                dist[i[0]] = now
                heapq.heappush(Q, (now, i[0]))  # heap에 추가

V, E = map(int, input().split())
K = int(input())
inf = 10**10
arr = [[] for _ in range(V+1)]
dist = [inf] * (V+1)        # 거리 리스트
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))   # 인접 리스트 만들기

dijkstra(K)
print(dist)
for i in dist[1:]:
    if i < inf:             # 경로가 있으면 출력
        print(i)
    else:                   # 없으면 INF 출력
        print('INF')
