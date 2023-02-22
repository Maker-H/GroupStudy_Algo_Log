from collections import deque
import sys; input = sys.stdin.readline

def bfs(a): # 탐색
    visitied = [0]*(n+1)
    q = deque()
    q.append(a)
    visitied[a] = 1
    while q:
        i = q.popleft()
        for j, k in tree[i]:
            if visitied[j] == 0:
                visitied[j] = visitied[i] + k # 시작점에서의 거리 갱신
                q.append(j)
    
    return max(visitied)-1

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])
ans = 0
for i in range(1,n+1): 
    if len(tree[i]) <= 1: # 리프 노드에 대해서 탐색
        tmp = bfs(i)

        if ans < tmp:
            ans = tmp

print(ans)