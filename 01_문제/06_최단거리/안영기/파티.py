# https://www.acmicpc.net/problem/1238
# [안영기] 다익스트라 / 파티 / 골드

import sys
import heapq
input = sys.stdin.readline


def dijkstra(E):                            # 최단 거리 구하기
    inf = 10**10
    dist = [inf] * (N+1)
    dist[E] = 0
    Q = []
    heapq.heappush(Q, (0, E))		    # Q에 heap형식으로 (가중치, 도착 노드)삽입

    while Q:
        d, now = heapq.heappop(Q)		# 최소힙이므로 가중치가 가장 작은 값이 pop
        if dist[now] >= d:					# D는 기본 inf로 삽입된 상태, 최솟값을 구했는지 확인
            for g, w in city[now]:		# city[now]와 연결된 노드들 확인
                if d + w < dist[g]:        # 최소값이면 갱신
                    dist[g] = d + w
                    heapq.heappush(Q, (d + w, g))   # 최소값이면 heapq에 추가
    return dist

N, M, X = map(int, input().split())
city = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    city[s].append([e, t])                  # 인접행렬 생성

ans = dijkstra(X)
ans[0] = 0

for i in range(1, N+1):
    if i != X:                              # X가 출발점인 경우 제외
        dist_1 = dijkstra(i)                # 모든 노드에서 X로 가는 최단시간
        ans[i] += dist_1[X]

print(max(ans))
