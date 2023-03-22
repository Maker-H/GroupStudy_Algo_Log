import heapq
import math
import sys
def dijkstra(K):
    dist = [math.inf] * (N + 1)     # 최단거리 초기값 INF로 설정
    Q = []
    heapq.heappush(Q,(0,K))         # 힙구조를 사용
    dist[K] = 0

    while Q:
        v, u = heapq.heappop(Q)

        for s in arr[u]:                    # 인접노드 확인
            weight = v + s[1]
            if weight < dist[s[0]]:         # 기존의 가중치와 비교 최단거리 테이블 업데이트
                dist[s[0]] = weight
                heapq.heappush(Q,(weight,s[0]))
    return dist

N, M, X = map(int,sys.stdin.readline().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,sys.stdin.readline().split()) # 매핑
    arr[u].append((v,w))

dist = dijkstra(X)      # X를 출발점으로 dijkstra
dist[0] = 0             # 출발점 0으로 지정

for i in range(1, N+1):
    if i != X:                  # X가 출발점인 경우는 제외
        dist_1 = dijkstra(i)
        dist[i] += dist_1[X]    # 최단시간 구하기

print(max(dist))
