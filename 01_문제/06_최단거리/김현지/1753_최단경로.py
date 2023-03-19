import heapq

def dijkstra(S):
    Q = []
    heapq.heappush(Q, (0, S))
    dist[S] = 0
    while Q:
        d, s = heapq.heappop(Q)
        if dist[s] < d:  # 최단 거리 아닐 경우
            continue

        for node, distance in arr[s]:
            if dist[node] > d + distance:  # 인접 노드로 가는 가중치가 최소보다 작다면
                dist[node] = d + distance  # 업데이트
                heapq.heappush(Q, (d+distance, node))


V, E = map(int, input().split())  # 정점, 간선
K = int(input())  # 시작 정점
INF = int(1e9)
dist = [INF] * (V+1)
arr = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())  # u에서 v로 가는 가중치 w
    arr[u].append((v, w))

dijkstra(K)
for i in dist[1:]:
    if i != INF:
        print(i)
    else:  # 경로 없다면
        print('INF')