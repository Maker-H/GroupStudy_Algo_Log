import sys
input = sys.stdin.readline


def find(x):
    if x == parent[x]:          # 부모노드로 자신을 가리키면 루트노드
        return x
    else:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:                  # 둘의 루트 노드가 다르면
        if x < y:               # 한 루트 노드를 다른쪽 루트노드 에 이어준다
            parent[x] = y
        else:
            parent[y] = x


N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

for i in range(1, N+1):
    edge = list(map(int, input().split()))
    for j in range(1, N+1):     # i번째 줄의 j번째 수는 연결정보를 의미
        if edge[j-1] == 1:      # 1부터 시작했으므로 -1을 해준다
            union(i, j)

travel = list(map(int, input().split()))
ans = set([find(i) for i in travel])
if len(ans) != 1:        # 둘의 경로가 같으면 ans의 길이는 1
    print('NO')
else:
    print('YES')





