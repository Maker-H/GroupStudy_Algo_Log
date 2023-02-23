# https://dogsavestheworld.tistory.com/111 - defaultdict 설명
# https://www.acmicpc.net/problem/17073
# 17073 [안영기] 트리 / 나무 위의 빗물 / 실버

import sys
from collections import defaultdict
input = sys.stdin.readline

N, W = map(int, input().split())

# 인접딕셔너리 만들기
tree = defaultdict(list)
for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

# 리프노드의 개수 카운팅
leaf_count = 0
for parentnode, childnode in tree.items():
    if parentnode != 1 and len(childnode) == 1:
        leaf_count += 1

print(round(W/leaf_count, 10))

