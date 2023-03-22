import heapq
import math
import sys
def dijkstra(K):
    Q = []
    heapq.heappush(Q,(0,K))             # 힙구조를 사용
    dist[K] = 0

    while Q:
        v, u = heapq.heappop(Q)

        for s in arr[u]:                            # 인접노드 확인
            weight = v + s[1]                       
            if weight < dist[s[0]]:                 # 기존의 가중치와 비교 최단거리 테이블 업데이트
                dist[s[0]] = weight
                heapq.heappush(Q,(weight,s[0]))


V,E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
arr = [[] for _ in range(V+1)]
dist = [math.inf] * (V+1)                                   # 최단거리 초기값 INF로 설정
for i in range(E):
    u,v,w = map(int,sys.stdin.readline().split())           #매핑
    arr[u].append((v,w))

dijkstra(K)

for i in range(1,V+1):
    if dist[i] != math.inf:     # INF가 아닐때 
        print(dist[i])          # 최단경로 출력
    else:
        print('INF')