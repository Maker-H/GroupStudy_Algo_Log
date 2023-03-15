import sys
import heapq

def shortest(K):
    heap = []
    # 힙은 제일 앞의 값을 기준으로 정렬하기에 가중치를 0에 두었다
    heapq.heappush(heap, (0, K))
    ws[K] = 0

    while heap:
        weight, v = heapq.heappop(heap)

        if ws[v] < weight:
            continue

        for new_node, new_weight in graph[v]:
                tmp_weight = new_weight + weight

                if ws[new_node] > tmp_weight:
                    ws[new_node] = tmp_weight
                    heapq.heappush(heap, (tmp_weight, new_node))



input = sys.stdin.readline
MAX = sys.maxsize

V, E = map(int, input().split())
K = int(input())

ws = [MAX] * (V + 1)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u] += [[v, w]]

shortest(K)

for i in range(1, V + 1):
    if ws[i] == MAX:
        print("INF")
    else:
        print(ws[i])

