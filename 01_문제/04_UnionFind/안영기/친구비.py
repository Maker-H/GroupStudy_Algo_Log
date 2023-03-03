# https://www.acmicpc.net/problem/16562
# [안영기] 분리 집합 / 친구비 / 골드

import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:              # 부모노드가 자신을 가리키면 루트 노드
        return x
    parent[x] = find(parent[x])     # 부모노드가 자신을 가리키지 않으면 부모 노드로 이동
    return parent[x]

def union(x, y):
    x = find(x)                     # 같은 집합인지 확인
    y = find(y)
    if x != y:                      # 서로 다른 집합인 경우
        if cost[x] <= cost[y]:      # 두 루트를 비교하여 가격이 더 저렴한 친구를 루트로
            parent[y] = x
        else:
            parent[x] = y


N, M, k = map(int, input().split())     # N : 학생 수, M : 친구관계 수, k : 가진 돈
cost = [0] + list(map(int, input().split()))
parent = [i for i in range(N+1)]       # 친구 리스트 생성
for i in range(M):
    v, w = map(int, input().split())
    union(v, w)

# parent = [0, 1, 2, 1, 2, 2]
tmp = set()
total = 0
for i in range(1, len(parent)):
    a = find(i)
    if a not in tmp:
        tmp.add(a)
        total += cost[a]

if total <= k:
    print(total)
else:
    print('Oh no')





