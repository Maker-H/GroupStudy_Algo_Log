import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)  # 방향성이 없으므로 반대 방향도 해줌

Q = int(sys.stdin.readline())
for _ in range(Q):
    t, k = map(int, input().split())
    if t == 1:
        if len(tree[k]) > 1:  # 연결된 선이 두개 이상이므로 단절점 가능
            print("yes")
        else:  # 자식이 하나만 있는 루트 노드거나 리프 노드일 경우 = 길이가 1일 때
            print("no")
    elif t == 2:  # 어떤 간선을 제거해도 그래프가 2개 이상으로 나뉨
        print("yes")