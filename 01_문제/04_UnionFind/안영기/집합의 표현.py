# https://www.acmicpc.net/problem/1717
# [안영기] 분리집합 / 집합의 표현 / 골드

import sys
sys.setrecursionlimit(10**6)    # 최대 재귀 가능 횟수를 조절
input = sys.stdin.readline

def find(x):
    if x == parent[x]:          # 부모노드로 자신을 가리키면 루트노드
        return x
    parent[x] = find(parent[x]) # 둘의 루트 노드가 다르면
    return parent[x]            # 두 루트를 비교하여 가격이 더 저렴한 친구를 루트로 연결


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())        # m : 연산의 개수
parent = list(map(int, range(n+1)))

for i in range(m):
    order, a, b = map(int, input().split())
    if order == 0:                      # 0이면 결합
        union(a, b)

    elif order == 1:                    # 1이면 연결되어 있는지 출력
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')

