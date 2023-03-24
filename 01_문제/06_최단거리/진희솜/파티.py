import sys
import heapq


def shortest_way_to_party(X):
    heap = []
    heapq.heappush(heap, [0, X])
    p_visited[X] = 0

    while heap:
        weight, vertex = heapq.heappop(heap)

        # 여기까지의 최단 경로보다 누적합이 더 크다면 건너뛴다
        if weight > p_visited[vertex]:
            continue

        for new_weight, new_vertex in graph[vertex]:
            # 누적합 구하기
            sum_w = new_weight + weight
            if sum_w < p_visited[new_vertex]:
                heapq.heappush(heap, [sum_w, new_vertex])
                p_visited[new_vertex] = sum_w

def shortest_way_to_home(X, home):
    heap = []
    heapq.heappush(heap, [0, home])
    h_visited[home] = 0

    if home == X:
        return 0

    while heap:
        weight, vertex = heapq.heappop(heap)

        if vertex == X:
            return weight

        # 여기까지의 최단 경로보다 누적합이 더 크다면 건너뛴다
        if weight > h_visited[vertex]:
            continue

        for new_weight, new_vertex in graph[vertex]:
            # 누적합 구하기
            sum_w = new_weight + weight

            if sum_w < h_visited[new_vertex]:
                heapq.heappush(heap, [sum_w, new_vertex])
                h_visited[new_vertex] = sum_w
    return -1


input = sys.stdin.readline
MAX = sys.maxsize

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
p_visited = [MAX] * (N + 1)

for _ in range(M):
    start, end, T = map(int, input().split())
    graph[start] += [[T, end]]

shortest_way_to_party(X)

ans = []
for home in range(1, N + 1):
    h_visited = [MAX] * (N + 1)
    tmp = shortest_way_to_home(X, home) + p_visited[home]
    ans.append(tmp)

print(max(ans))