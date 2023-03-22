import sys
import heapq
input = sys.stdin.readline

# 다익스트라 알고리즘
def dijkstra(start):
    distance = [1e9] * (N + 1)
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weight, now = heapq.heappop(heap)

        if distance[now] < weight:
            continue

        for w, v in graph[now]:
            tmp = weight + w
            if tmp < distance[v]:
                distance[v] = tmp
                heapq.heappush(heap, (tmp, v))

    return distance


N, M, X = map(int,input().split())


heap = []
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int,input().split())
    graph[u].append((w, v))

ans = 0
for i in range(1, N+1):
    # go, back 가는길 오는길 따로 다익스트라 실행
    go = dijkstra(i)
    back = dijkstra(X)
    ans = max(ans, go[X] + back[i])

print(ans)