def bfs(v):
    Q = deque()
    Q.append(v)
    isTree = True

    while Q:
        k = Q.popleft()
        if visited[k] == 1:
            isTree = False
        visited[k] = 1
        for w in arr[k]:
            if visited[w] == 0:
                Q.append(w)

    return isTree



import sys
from collections import deque
sys.setrecursionlimit(10000000)
t = 0
while True:
    t += 1
    N,M = map(int,sys.stdin.readline().split())
    arr = {i : []for i in range(N+1)}
    visited = [0] * (N+1)
    if N == 0 and M == 0:
        break

    for _ in range(M):
        S,E = map(int,sys.stdin.readline().split())
        arr[S].append(E)
        arr[E].append(S)

    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 1:
            pass
        if bfs(i) == True:
            cnt += 1

    if cnt == 0:
        print(f'Case {t}: No trees.')
    elif cnt == 1:
        print(f'Case {t}: There is one tree.')
    else:
        print(f'Case {t}: A forest of {cnt} trees.')



