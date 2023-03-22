import sys
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = -1
    graph[b][a] = 1

# 플루이드-와샬 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == 0:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    # 경유하는 곳까지 포함 모든 경우가 1인 경우 1
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    # 경우하는 곳까지 포함 모든 경우가 -1인 경우 -1
                    graph[i][j] = -1
                # 유추할 수 없는 경우는 0

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(graph[a][b])
