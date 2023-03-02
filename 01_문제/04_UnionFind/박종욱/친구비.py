def find_(x):           # 부모노드 찾는 함수
    if arr[x] == x:
        return arr[x]
    else:
        arr[x] = find_(arr[x])
    return arr[x]

def union(x,y):         # 집합 합치는 함수
    x_ = find_(x)       # x의 부모노드
    y_ = find_(y)       # y의 부모노드

    if friend[x_] < friend[y_]:         # 친구비가 더 비쌀경우 친구비가 싼 배열을 부모노드로
        arr[y_] = x_
    else:
        arr[x_] = y_



import sys
sys.setrecursionlimit(1000000)

N,M,K = map(int,sys.stdin.readline().split())
arr = [i for i in range(N+1)]
friend = [0] + list(map(int,sys.stdin.readline().split()))

for _ in range(M):                                  # 양방향 매핑
    S,E = map(int,sys.stdin.readline().split())
    union(S,E)


a =0
for t in range(1,N+1):
    if t == find_(t):               # 만약 인덱스와 그 인덱스에 해당되는 부모노드의 값이 같을경우(다른트리)
        a += friend[t]              # 친구비 추가


if a <= K:                                        # 트리가 없는경우
    print(f'{a}')

else:                                               # 트리가 여러개인 경우
    print(f'Oh no')



