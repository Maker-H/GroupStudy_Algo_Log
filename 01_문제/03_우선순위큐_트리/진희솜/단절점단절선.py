import sys

N = int(sys.stdin.readline())

tree = {node:[] for node in range(1, N+1)}

for _ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1] += [n2]
    tree[n2] += [n1]


R = int(sys.stdin.readline())
for _ in range(R):
    t, k = map(int, sys.stdin.readline().split())

    # 루트 :  부모x, 자식 0 or 1 -> 0, 1
    # 리프 : 부모 1, 자식 0 -> 1
    if t == 1:
        if len(tree[k]) < 2:
            print("no")
        else:
            print("yes")

    # 어떤 간선이던간에 단절선일 수 밖에 없다
    elif t == 2:
        print("yes")



