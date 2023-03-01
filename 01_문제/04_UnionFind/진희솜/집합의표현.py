import sys
sys.setrecursionlimit(10**6)

def union_sets(a, b):
    if a == b:
        return
    root_a = find(a)
    root_b = find(b)

    if root_a < root_b:
        parent[root_b] = root_a
    elif root_a > root_b:
        parent[root_a] = root_b

def find(num):
    # 자기 자신 가리킨다면 루트임으로 계속 타고 올라가준다
    # 배열 상에서 왔다갔다 하면 logN이므로 경로압축 사용해 상수시간으로 줄여보자
    if parent[num] != num:
        parent[num] = find(parent[num])

    return parent[num]
    

n, m = map(int, sys.stdin.readline().split())
# 자기 자신을 가리키는 집합 만들기
parent = [i for i in range(n + 1)]


for idx in range(m):
    check, a, b = map(int, sys.stdin.readline().split())

    # 집합 만들기
    if check == 0:
        union_sets(a, b)
        
    if check == 1:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')


