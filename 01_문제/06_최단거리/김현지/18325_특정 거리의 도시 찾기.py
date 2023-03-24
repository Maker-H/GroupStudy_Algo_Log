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


N, M, K, X = map(int, input().split())  # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
INF = int(1e9)
dist = [INF] * (N+1)
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())  # A에서 B로 이동하는 단방향
    arr[A].append((B, 1))
dijkstra(X)

ans = []
for i in range(1, N+1):
    if dist[i] == K:  # 최단 거리 K인 도시가 존재하면
        ans.append(i)

if len(ans):
    for i in ans:
        print(i)
else:
    print(-1)