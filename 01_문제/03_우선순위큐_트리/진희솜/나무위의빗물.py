from sys import stdin
import sys
sys.setrecursionlimit(10**6)

def dfs(node, water):
    visited[node] = True   
    # 부모가 무조건 포함되어 있으므로 -1 해준다
    child_num = len(tree[node]) - 1

    if child_num == 0:
        return ans.append(water)
    
    # 확률 계산
    for child in tree[node]:
        if visited[child] == False:
            dfs(child, water / child_num)


N, W = map(int, stdin.readline().split())
tree = {node:[] for node in range(1, N + 1)}
visited = {node:False for node in range(1, N + 1)}
ans = []

for _ in range(N - 1):
    U, V = map(int, stdin.readline().split())
    tree[U] += [V]
    tree[V] += [U]

# 1은 부모가 없으므로 따로 계산
visited[1] = True
for i in tree[1]:
    dfs(i, W/len(tree[1]))

print(sum(ans)/len(ans), 10)