def bellman_ford(S):
    dist[S] = 0
    for i in range(N):
        for j in range(M):
            cur_node = arr[j][0]
            next_node = arr[j][1]
            weight = arr[j][2]
            # 현재 간선을 거쳐 다른 노드로 이동 했을 때 거리가 더 짧다면
            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + weight:
                dist[next_node] = dist[cur_node] + weight
                if i == N-1:  # N 번째에도 그런 경우
                    return True
    return False


N, M = map(int, input().split())
arr = []
INF = int(1e9)
dist = [INF] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())  # 시작 도시, 도착 도시, 이동 시간
    arr.append((A, B, C))

if bellman_ford(1):  # 시간이 되돌아 가는 경우
    print("-1")
else:
    for i in range(2, N+1):
        if dist[i] == INF:  # 해당 도시로 가는 경로 없는 경우
            print("-1")
        else:
            print(dist[i])