import sys
import heapq
input = sys.stdin.readline

# 다익스트라 알고리즘
def dijkstra(start):
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


V, E = map(int, input().split())
start = int(input())

distance = [1e9]*(V+1)
heap = []
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((w, v))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])