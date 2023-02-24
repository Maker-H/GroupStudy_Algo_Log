import sys
from collections import deque


def trunk(root):
    global trunk_len
    Q = deque()
    Q.append(root)
    last_node_key = 0

    while Q:
        current_key = Q.popleft()

        # 루트는 부모가 없기에 고려해준다
        if current_key == root and len(tree[current_key]) >= 2:
            return root
        elif current_key != root and len(tree[current_key])-1 > 2:
            return current_key
        else:
            last_node_key = current_key

        for w in tree[current_key]:
            w_key = w[0]
            w_weight = w[1]

            # visited를 sum배열로 활용
            if visitied[w_key] == 0 and w_key != root:
                visitied[w_key] = visitied[current_key] + w_weight
                trunk_len = visitied[w_key]
                Q.append(w_key)

    return last_node_key


def from_giga_to_leaf(root):
    global giga_len
    Q = deque()

    Q.append(root)

    while Q:
        current_key = Q.popleft()

        for w in tree[current_key]:
            node_key = w[0]
            node_weight = w[1]

            # visited를 sum배열로 활용
            if visitied[node_key] == 0 and node_key != root:
                visitied[node_key] = visitied[current_key] + node_weight

                if giga_len < visitied[node_key]:
                    giga_len = visitied[node_key]

                Q.append(node_key)


N, R = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(N+1)]
visitied = [0] * (N+1)
for _ in range(N-1):
    a, b, d = map(int, sys.stdin.readline().split())
    tree[a].append([b, d])
    tree[b].append([a, d])

# 먼저 기둥 길이 구하면서 + 기가 노드 구하기
trunk_len = 0
giga = trunk(R)



# 기가 노드를 루트로 제일 긴 가지 구하기
giga_len = 0
visitied[giga] = 0 # 기가 노드부터 방문 체크하기 위해서 0으로 만들어줌
from_giga_to_leaf(giga)
print(trunk_len, giga_len)

