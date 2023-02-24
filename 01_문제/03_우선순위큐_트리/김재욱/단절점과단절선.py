import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    if t == 2: # 단절선의 경우 무조건 2개의 서브트리가 생긴다.
        print('yes')

    else:
        if len(tree[k]) <= 1: # 말단 노드 일때
            print('no')
        else:
            print('yes')