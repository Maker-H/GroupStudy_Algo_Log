import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

# 플로이드 와샬 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 1e9:
            print(0, end= ' ')

        else:
            print(graph[i][j], end = ' ')
    print()