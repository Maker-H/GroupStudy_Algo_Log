import sys
input = sys.stdin.readline


def bellman_ford(start):
    distance[start] = 0
    for i in range(N):
        # 매 반복마다 모든간선 확인
        for j in range(M):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != 1e9 and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == N-1:
                    # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                    return False

    return True


N, M = map(int,input().split())
distance = [1e9]*(N+1)
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())

    edges.append((a, b, c))

flag = bellman_ford(1)

if not flag:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == 1e9:
            print(-1)
        else:
            print(distance[i])