from collections import deque

def bfs(v):
    # enQ + visited 설정
    Q = deque()
    Q.append(v)
    visited = [0] * (N + 1)  # 매번 방문체크 해야하므로
    visited[v] = 1

    # Q가 비어있지 않은 동안
    while Q:
        # v = deQ
        v = Q.popleft()
        # v에 인접한 정점 중에서 방문 안한 정점이면
        for x, y in tree[v]:
            if not visited[x]:
                # enQ + visited 설정
                Q.append(x)
                visited[x] = visited[v] + y  # 가중치만큼 더함

    return max(visited)-1  # 가장 큰 값 리턴


N = int(input())
tree = {i : [] for i in range(N+1)}

for _ in range(N-1):
    p, c, w = map(int, input().split())  # p: 부모, c: 자식, w: 가중치
    tree[p].append([c, w])
    tree[c].append([p, w]) # 방향성 없으므로


cnt = 0
for i in range(N+1):
    b = bfs(i)
    if cnt < b:
        cnt = b  # 최대 길이(= 지름)

print(cnt)
