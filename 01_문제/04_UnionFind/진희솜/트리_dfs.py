import sys
sys.setrecursionlimit(10**6)

def dfs(current):
    for w in graph[current]:
        # 아래에서 무방향으로 노드를 저장했기에
        # current와 연결되어 있는 노드가 current의 부모일 수 있다
        # current의 부모인 노드라면 부모 노드를 타고 current로 왔을 것임으로 이중 확인이 된다
        if parent[current] == w:
            continue

        parent[w] = current

        # current의 부모가 아닌데 visited가 되어 있다면 이건 트리가 순환한다는 뜻이다
        if visited[w] != 0:
            return False

        visited[w] = 1
        # 리턴값 받아서 반환하게 해봤는데 global 선언하는게 더 쉬울거 같다
        if dfs(w) == False:
            return False

    return True


test_case = 1

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0:
        break
    graph = [[] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    parent = [0] * (N + 1)

    for _ in range(M):
        n1, n2 = map(int, sys.stdin.readline().split())
        graph[n1] += [n2]
        graph[n2] += [n1]

    cnt = 0
    # 유니온 파인드로 시작하는 노드의 루트는 자기 자신으로 설정해줌
    for node in range(1, N+1):

        if visited[node] == 0:
            parent[node] = node
            visited[node] = 1
            is_tree = dfs(node)
            if is_tree == True:
                cnt += 1

    if cnt == 0:
        print(f'Case {test_case}: No trees.')
    elif cnt == 1:
        print(f'Case {test_case}: There is one tree.')
    elif cnt > 1:
        print(f'Case {test_case}: A forest of {cnt} trees.')

    test_case += 1