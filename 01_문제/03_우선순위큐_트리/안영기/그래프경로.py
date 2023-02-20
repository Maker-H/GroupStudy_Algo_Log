import sys
sys.stdin = open('그래프경로.txt')

def dfs(v):
    visited[v] = 1
    if v == G:
        global flag
        flag = 1
        return

    for w in range(V+1):
        if adj_m[v][w] == 1 and visited[w] == 0:
            dfs(w)
    return 0

T = int(input())
for testcase in range(1, T+1):
    V, E = map(int, input().split())

    adj_m = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    flag = 0

    for _ in range(E):
        s, e = map(int, input().split())
        adj_m[s][e] = 1
    S, G = map(int, input().split())
    dfs(S)
    print(f'#{testcase} {flag}')


# def dfs(v): # 시작정점
#     # 방문체크
#     visited[v] = 1
#
#     # 시작정점(v)에 인접하고 방문안한 정점
#     for w in range(1, V+1):
#         if adj_m[v][w] == 1 and visited[w] == 0:
#             # 재귀호출
#             dfs(w)
#
# T = int(input())
# for testcase in range(1, T+1):
#     V, E = map(int, input().split())
#     # 인접행렬
#     adj_m = [[0] * (V+1) for _ in range(V+1)]
#     # 방문체크
#     visited = [0] * (V+1)
#     # 인접행렬에 저장
#     for _ in range(E):
#         a, b = map(int, input().split())
#         adj_m[a][b] = 1     # 방향성 있음
#     # 출발점, 도착점 입력
#     S, G = map(int, input().split())
#     dfs(S)
#     print(f'#{testcase} {visited[G]}')
