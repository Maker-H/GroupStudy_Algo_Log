def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1          # 방문체크
    while Q:
        v = Q.pop(0)
        print(v,end = ' ')  # 출력
        for w in range(1,N+1):
            if visited[w] == 0 and arr[v][w] == 1:
                Q.append(w)
                visited[w] = 1


def dfs(v):
    visited[v] = 1              # 방문체크
    print(v,end=' ')            # 출력
    for w in range(1,N+1):
        if visited[w] == 0 and arr[v][w]==1:
            dfs(w)


N,M,V = map(int,input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
visited =[0] *(N+1)
for _ in range(M):
    A,B = map(int,input().split())      # 양방향 매핑
    arr[A][B] = 1
    arr[B][A] = 1
dfs(V)
print()
visited =[0] *(N+1)     # visited 사용되었으니 초기화
bfs(V)
