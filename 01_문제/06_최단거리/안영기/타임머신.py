# https://www.acmicpc.net/problem/11657
# [안영기] 다익스트라 / 타임머신 / 골드

def bf(S):
    dist[S] = 0             # 시작노드 초기화
    for i in range(1, N+1):
        # 매 반복마다 모든 간선 확인
        for j in range(M):
            cur, n_node, cost = edges[j][0], edges[j][1], edges[j][2]
            # 최소값이면 갱신
            if dist[cur] != inf and dist[n_node] > dist[cur] + cost:
                dist[n_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신되면 음수 순환 존재
                if i == N:
                    return True
    return False

N, M = map(int, input().split())
edges = []
inf = 10**10
dist = [inf] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))


ans = bf(1)

if ans:         # n번째 라운드에서도 값이 갱신되면 음수 순환 존재
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == inf:  # 도달할 수 없으면 -1 출력
            print(-1)
        else:               # 도달 가능하면 최소거리 출력
            print(dist[i])


