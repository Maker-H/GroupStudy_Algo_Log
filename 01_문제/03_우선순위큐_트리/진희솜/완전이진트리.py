from sys import stdin

def recur(tree, level, max_level):
    # 트리 끝에 도달하면 반환
    if level == max_level:
        return

    # 전달 받은 리스트에서 루트 찾기
    root_idx = len(tree) // 2

    # 루트를 레벨에 따라 리스트에 넣기
    split_tree[level].append(tree[root_idx])

    # 왼쪽 서브트리, 오른쪽 서브트리로 재귀적 호출
    recur(tree[:root_idx], level + 1, max_level)
    recur(tree[root_idx + 1:], level + 1, max_level)



L = int(stdin.readline())
tree = list(map(int, stdin.readline().split()))
split_tree = [[] for _ in range(L)]
recur(tree, 0, L)

for lst in split_tree:
    print(" ".join(map(str, lst)))