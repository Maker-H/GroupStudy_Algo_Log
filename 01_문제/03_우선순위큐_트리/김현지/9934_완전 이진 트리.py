def b_tree(S, E, L):  # Start, End, Level
    if S == E:  # 하나만 남으면
        tree[L].append(arr[S])  # 트리에 삽입
        return
    mid = (S + E) // 2
    tree[L].append(arr[mid])  # 중간이 트리의 루트
    b_tree(S, mid-1, L + 1)  # 재귀 이용
    b_tree(mid+1, E, L + 1)


K = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(len(arr) + 1)]
b_tree(0, len(arr)-1, 0)

for t in tree:
    print(*t)