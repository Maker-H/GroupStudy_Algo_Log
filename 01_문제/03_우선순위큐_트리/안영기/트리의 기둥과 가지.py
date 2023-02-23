# https://www.acmicpc.net/problem/20924
# 20924 [안영기] 트리 / 트리의 기둥과 가지 / 골드

import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    visited = [0] * (N+1)
    visited[v] = 1
    Q = deque([[v, 0]])         # 노드 번호와 누적 거리로 구성된 요소

    max_val = 0
    flag = 0
    while Q:
        now, now_w = Q.popleft()

        if flag == 0 and len(adjl[now]) > 2:        # flag를 이용해 기가노드 시점의 누적거리 체크
            ans = now_w
            flag = 1

        if flag == 0 and len(adjl[now]) > 1 and now == v:       # 루트노드가 기가노드인 테스트 케이스 대비
            ans = 0
            flag = 1

        for child, child_w in adjl[now]:
            if not visited[child]:                      # 미방문 노드일 경우 방문체크 후, 거리 누적, 큐에 쌓기
                visited[child] = 1
                W = now_w + child_w
                Q.append([child, W])
                if W > max_val:                         # 기가노드~리프노드의 최대 거리 확인
                    max_val = W

    if flag == 1:
        return ans, max_val-ans
    else:
        return now_w, 0



N, R = map(int, input().split())
adjl = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, d = map(int, input().split())     # 부모노드, 자식노드, 거리
    adjl[a].append([b, d])                  # 트리는 방향성이 없으므로 양쪽 모두에 연결
    adjl[b].append([a, d])

answer = bfs(R)
print(*answer)



