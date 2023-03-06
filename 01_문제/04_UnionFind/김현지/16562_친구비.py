from collections import deque


def bfs(v):
    Q = deque()
    Q.append(v)

    while Q:
        v = Q.popleft()
        visited[v] = 1  # 방문 체크
        tree_node.append(v)  # 리스트에 삽입
        for w in adj_list[v]:
            if not visited[w]:  # v에 인접한 정점 중에서 방문 안한 정점이면
                Q.append(w)


N, M, K = map(int, input().split())  # N: 학생 수, M: 친구관계 수, k: 가지고 있는 돈
arr = list(map(int, input().split()))  # 친구비 리스트
adj_list = {i: [] for i in range(1, N + 1)}
visited = [0] * (N + 1)
for _ in range(M):
    v, w = map(int, input().split())
    adj_list[v].append(w)
    adj_list[w].append(v)

arr_min_list = []  # 최소 비용 리스트
for i in range(1, N + 1):
    tree_node = []  # 트리 노드 리스트
    arr_min = 987654321
    if visited[i] == 0:
        bfs(i)
        for n in tree_node:  # 각 트리별로 노드들 중에서
            if arr_min > arr[n - 1]:  # 친구비 리스트를 통해 최소 비용 찾기
                arr_min = arr[n - 1]
        arr_min_list.append(arr_min)  # 최소 비용 삽입

cnt = 0
for a in arr_min_list:  # 친구 사귈 수 있는 최소 비용 다 더하기
    cnt += a
if cnt > K:  # 최소 비용이 가지고있는 돈보다 더 크면
    print("Oh no")
else:
    print(cnt)