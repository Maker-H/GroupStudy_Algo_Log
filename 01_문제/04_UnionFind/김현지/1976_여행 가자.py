def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        x, y = y, x
    parent[x] = y
    if x == y:
        y += 1

N = int(input())  # 도시의 수
M = int(input())  # 여행 계획에 속한 도시들의 수
arr = [[0]*(N+1)]+[[0] +list(map(int, input().split())) for _ in range(N)]
# 도시의 번호가 1부터 시작이어서 0을 2차원 배열에 넣음
parent = [i for i in range(N+1)]  # 노드의 부모노드 확인 리스트
plan = list(map(int, input().split()))

for i in range(N+1):
    for j in range(0, i+1):
        if arr[i][j] == 1:  # 연결
            union(i, j)
ans = "YES"
for k in range(len(plan)-1):
    if find(plan[k]) != find(plan[k+1]):  # 두 도시가 연결되어 있지 않다면
        ans = "NO"
print(ans)