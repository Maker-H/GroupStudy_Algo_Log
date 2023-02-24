# https://www.acmicpc.net/problem/9934
# 9934 [안영기] 트리 / 완전이진트리 / 실버

# 중위 순회 형식
def make_tree(arr, idx):               # 부모노드를 찾아 인덱스를 차례대로 채우기

    mid = len(arr)//2                  # 배열의 가운데 오는 노드가 부모노드
    tree[idx].append(arr[mid])

    if len(arr) == 1:
        return

    make_tree(arr[:mid], idx+1)        # 왼쪽 자식노드
    make_tree(arr[mid+1:], idx+1)      # 오른쪽 자식노드


level = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(level)]

make_tree(nums, 0)                      # 첫번째 인덱스(루트) 채우기

for lst in tree:
    print(*lst)




# def make_tree(arr, idx):
#
#     mid = len(arr)//2
#     tree[idx].append(arr[mid])
#
#     if len(arr) == 1:
#         return
#
#     make_tree(arr[:mid], idx+1)
#     make_tree(arr[mid+1:], idx+1)
#
#
# level = int(input())
# nums = list(map(int, input().split()))
# tree = [[] for _ in range(level)]
#
# make_tree(nums, 0)
#
# for lst in tree:
#     print(*lst)






