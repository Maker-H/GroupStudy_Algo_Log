import sys


def find(x):
    while parent[x] != x:
        x = parent[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        x, y = y, x
    parent[x] = y
    if x == y:
        y += 1


N, M = map(int, sys.stdin.readline().split())  # M : 연산의 개수
parent = [i for i in range(N + 1)]  # 노드의 부모 노드 확인 리스트, 처음엔 자기 자신
for _ in range(M):
    n, a, b = map(int, sys.stdin.readline().split())
    if n == 0:  # 합집합 만들기
        union(a, b)
    elif n == 1:  # 두 원소가 같은 집합에 포함되어 있는지 확인
        a = find(a)
        b = find(b)
        if a == b:
            print("YES")
        else:
            print("NO")
