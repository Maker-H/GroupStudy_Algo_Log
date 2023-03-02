
from collections import deque


def bfs(v):
    Q = deque()
    Q.append(v)
    flag = 0

    while Q:
        v = Q.popleft()
        if visited[v] == 1:  # 방문한 노드이면 (사이클 체크)
            flag = 1
        visited[v] = 1  # 방문
        for w in adj_list[v]:
            if not visited[w]:  # v에 인접한 정점 중에서 방문 안한 정점이면
                Q.append(w)
    return flag


tc = 1
while True:
    N, M = map(int, input().split())  # N:정점 개수, M: 간선 개수

    if N == 0 and M == 0:
        break

    adj_list = {i: [] for i in range(1, N + 1)}
    visited = [0] * (N + 1)
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    tree_cnt = 0  # 트리 개수
    for i in range(1, N + 1):
        if visited[i] == 0:  # 방문하지 않는 노드일 때
            flag = bfs(i)
            if flag == 0:  # 트리가 있는 경우
                tree_cnt += 1  # 트리 개수 +1

    if flag == 1:  # 트리 없다면
        print(f'Case {tc}: No trees.')
    else:  # 트리 있다면
        if tree_cnt > 1:
            print(f'Case {tc}: A forest of {tree_cnt} trees.')
        elif tree_cnt == 1:
            print(f'Case {tc}: There is one tree.')

    tc += 1