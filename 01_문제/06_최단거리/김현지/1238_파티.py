import heapq

def dijkstra(S):
    dist = [INF] * (N + 1)
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
    return dist

N, M, X = map(int, input().split())  # 학생 수, 단방향 도로, 시작 정점
INF = int(1e9)
arr = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())  # 시작, 끝, 소요 시간
    arr[s].append((e,t))


cnt = dijkstra(X)
cnt[0] = 0

for i in range(1, N+1):
    if i != X:  # 출발 마을 아닐 때
        ans = dijkstra(i)
        cnt[i] += ans[X]

print(max(cnt))  # 최대값