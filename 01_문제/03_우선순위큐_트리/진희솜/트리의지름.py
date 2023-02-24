import sys
from collections import deque
def bfs(root, tree_sum):
    global tree_max
    Q = deque()
    Q.append(root)
    max_node = 0

    while Q:
        v = Q.popleft()
        
        for w in tree[v]:
            node = w[0]
            W = w[1]

            # visited를 sum 배열로 사용했기에 정점 1은 방문체크가 안되므로
            # and로 예외처리 함
            if visited[node] == 0 and node != root:

                # visited를 sum 배열로 사용
                visited[node] = visited[v] + W

                if tree_max < visited[node]:
                    tree_max = visited[node]
                    max_node = node

                Q.append(node)

    return max_node






N = int(sys.stdin.readline())
visited = [0] * (N+1)
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    P, C, W = map(int, sys.stdin.readline().split())
    tree[P].append([C,W])
    tree[C].append([P,W])

tree_max = 0

# 정점 1에서 제일 멀리 있는 노드 찾기
node = bfs(1, 0)

# 제일 멀리 있는 노드를 루트로 제일 먼 거리를 tree_max에 저장
visited = [0] * (N+1)
bfs(node, 0)

print(tree_max)

