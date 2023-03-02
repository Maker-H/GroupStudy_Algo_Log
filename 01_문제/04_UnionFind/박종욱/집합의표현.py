def find_(x):           # 부모노드 찾는 함수
    if arr[x] == x:
        pass
    else:
        arr[x] = find_(arr[x])
    return arr[x]

def union(x,y):         # 집합 합치는 함수
    x_ = find_(x)       # x의 부모노드
    y_ = find_(y)       # y의 부모노드

    if x_ < y_:         # 더큰값의 부모를 작은값으로 설정
        arr[y_] = x_
    else:
        arr[x_] = y_

import sys
sys.setrecursionlimit(100000)                # 파이썬 재귀깊이가 정해져있어서 recursion error 나와서 깊이를 늘려줌

N,M = map(int,sys.stdin.readline().split())  # N : 노드의 개수 M : 연산의 개수
arr = [i for i in range(N+1)]                # 부모의 노드값만 바꿔주면 되어서 리스트로 만듬

for _ in range(M):
    A,B,C = map(int,sys.stdin.readline().split())
    if A == 0:
        union(B,C)

    else:
        if find_(B) == find_(C):            # 서로의 부모노드가 같다면(같은트리)
            print('YES')    
        else:                               # 다르다면
            print('NO')
