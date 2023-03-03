def find_(x):           # 부모노드 찾는 함수
    if arr[x] == x:
        return arr[x]
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

N = int(sys.stdin.readline())    # 도시의 수 (노드의 수)
M = int(sys.stdin.readline())    # 여행계획 도시의 수
arr = [i for i in range(N+1)]
for i in range(1,N+1):
    arr_1 = [0] +list(map(int,sys.stdin.readline().split()))       # 간선
    for s in range(1,len(arr_1)):
        if arr_1[s] == 1:
            union(i,s)

arr_2 = [0] + list(map(int,sys.stdin.readline().split()))     # 여행계획도시
flag = 0
for i in range(1,len(arr_2)-1):
    if arr[arr_2[i]] == arr[arr_2[i+1]]:        # 같은 트리일때 flag = 0
        flag = 0
    else:                                       # 다른트리가 나오면 flag =1 break
        flag = 1
        break

if flag == 0:
    print('YES')
else:
    print('NO')