import sys
from collections import deque


def bfs(node):
    Q = deque()
    Q.append(node)
    is_tree  = True
    while Q:
        v = Q.popleft()

        # 전체 다 돌았는데 중간에 하나라도 겹치는게 있다면 그래프이다
        if visited[v] == 1:
            is_tree = False

        visited[v] = 1
        for w in graph[v]:
            if visited[w] == 0:
                Q.append(w)
    return is_tree

test_case = 1

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0:
        break

    graph = [[] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        n1, n2 = map(int, sys.stdin.readline().split())
        graph[n1] += [n2]
        graph[n2] += [n1]

    cnt = 0
    for node in range(1, N + 1):
        if visited[node] == 0:
            is_tree = bfs(node)
            if is_tree == True:
                cnt += 1

    if cnt == 0:
        print(f'Case {test_case}: No trees.')
    elif cnt == 1:
        print(f'Case {test_case}: There is one tree.')
    elif cnt > 1:
        print(f'Case {test_case}: A forest of {cnt} trees.')

    test_case += 1