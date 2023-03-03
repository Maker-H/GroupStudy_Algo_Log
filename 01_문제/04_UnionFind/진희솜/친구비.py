import sys
sys.setrecursionlimit(10**6)

def dfs(current):
    global smallest
    for w in tree[current]:
        if w == parent[current]:
            continue
        parent[w] = current

        # 그래프라면 이제 그만 돌아도 된다
        if visited[w] != 0:
            return
        visited[w] = 1

        if student_money[w] < smallest:
            smallest = student_money[w]

        dfs(w)

    return



N, M, MONEY = map(int, sys.stdin.readline().split())

# 노드랑 인덱스 맞춰주기
student_money = [0] + list(map(int, sys.stdin.readline().split()))

tree = [[] * (N + 1) for _ in range(N + 1)]
parent = [0] * (N + 1)
visited = [0] * (N + 1)

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())

    # 같은 관계 들어올 경우 패쓰!
    if n1 == n2:
        continue

    # 이미 있는 경우 추가할 필요 없음
    if n2 not in tree[n1]:
        tree[n1] += [n2]
    if n2 not in tree[n2]:
        tree[n2] += [n1]

mins = []
for node in range(1, N + 1):
    if visited[node] == 0:
        smallest = student_money[node]
        parent[node] = node
        visited[node] = 1

        dfs(node)
        mins.append(smallest)

if sum(mins) > MONEY:
    print('Oh no')
else:
    print(sum(mins))