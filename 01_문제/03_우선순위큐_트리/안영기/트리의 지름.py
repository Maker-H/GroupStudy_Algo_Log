# https://www.acmicpc.net/problem/1967
# 1967 [안영기] 트리 / 트리의 지름 / 골드

import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    global max_val
    global max_node
    visited = [0] * (n+1)

    Q = deque([[v, 0]])
    visited[v] = 1              # 방문체크

    while Q:
        now, now_w = Q.popleft()    # 현재 노드와 현재노드까지 쌓인 거리
        for child, child_w in adjd[now]:        # 현재 노드의 자식노드
            if not visited[child]:              # 방문하지 않았으면
                visited[child] = 1              # 방문체크
                Q.append([child, now_w + child_w])  # Q 대기열에 추가, 거리 추가
                if now_w + child_w > max_val:
                    max_val = now_w + child_w
                    max_node = child
    return max_val


n = int(input())
adjd = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, input().split())     # 부모노드, 자식노드, 거리
    adjd[p].append([c, w])                  # 트리는 방향성이 없으므로 양쪽 모두에 연결
    adjd[c].append([p, w])

max_val = 0
max_node = 1

bfs(1)                      # 루트노드에서 가장 멀리 있는 리프노드 탐색
print(bfs(max_node))        # 루트노드에서 가장 먼 리프노드에서 가장 먼 리프노드 -> 지름의 길이


