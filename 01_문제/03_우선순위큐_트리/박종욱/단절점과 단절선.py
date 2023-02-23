import sys


T = int(sys.stdin.readline())
arr = {i : [] for i in range(T+1)}                      # 인덱스와 리스트 생성
for tc in range(T-1):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)                                    # 인접점 추가
    arr[b].append(a)

N = int(sys.stdin.readline())
for i in range(N):
    t,k = map(int,sys.stdin.readline().split())
    if t == 1:                                          # 단절점에 대해 판별
        if len(arr[k]) <= 1:                            # k번 정점의리스트원소의 수가 1보다 적으면
            print('no')                                 # 단절점이 아님
        else:
            print('yes')                                # 많으면 단절점
    else:                                               # 단절선에 대해 판별
        if arr[k]:                                      # k번 정점에 값이 있으면 
            print('yes')                                # 단절선
        else:                                           # 없으면 단절선이 아님
            print('no')


