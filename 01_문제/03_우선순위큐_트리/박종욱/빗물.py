import sys
from collections import deque


def solve(i):
    global cnt
    Q = deque()                 # enqueue
    Q.append(i)
    visited[i] = 1              #방문점 체크

    while Q:                    # Q에 값이 존재하는동안
        s = Q.popleft()
        if len(arr[s]) == 1 and visited[arr[s][0]]:     # 리프노드의 조건
            cnt += 1

        for w in arr[s]:        
            if not visited[w]:
                Q.append(w)
                visited[w] = 1

    return


T,K = map(int,sys.stdin.readline().split()) # T:노드의 개수   K:물의양
arr = {i : [] for i in range(T+1)}  # 인덱스와 리스트 생성
visited = [0] * (T + 1)             # 방문점 생성
for tc in range(T-1):
    U, V = map(int,sys.stdin.readline().split())
    arr[U].append(V)
    arr[V].append(U)

cnt = 0             # 리프노드의 수를 셀 cnt
solve(1)            # 노드1에서 시작

print(K/cnt)
