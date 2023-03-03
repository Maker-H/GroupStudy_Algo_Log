# https://www.acmicpc.net/problem/18111
# [안영기] 브루트포스 / 마인크래프트 / 실버

import sys
input = sys.stdin.readline

def check(a, b):    # a : 평탄화하려는 높이, b : 가용가능 블럭 수
    sec = 0     # 걸리는 시간
    c = 0       # a보다 아래쪽에 있어 채워야 하는 블록의 개수
    for i in range(N):
        for j in range(M):
            z = arr[i][j] - a
            if z > 0:       # 높이가 측정하려는 높이보다 높으면
                b += z      # 블럭을 빼서 인벤토리에 저장하므로 가용가능한 블럭 수 추가
                sec += 2*z  # 블럭을 제거하는데에는 2초
            else:
                c -= z      # 측정하려는 높이보다 낮으면 블럭을 쌓아야 함  +1초
    if b < c:               # 가용가능 블럭보다 필요 블럭이 많으면
        return 10**10       # 최소 값을 찾고 있으므로 큰 수를 줘서 사용 x
    return sec + c          # 평탄화 수행 가능하면 걸리는 시간을 출력


N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

min_h = min([min(x) for x in arr])      # 가장 낮은 높이 탐색
max_h = max([max(x) for x in arr])      # 가장 높은 높이 탐색

min_sec = 10**10

# 가장 높은높이부터 가장 낮은 높이까지, 모든 지형을 해당 높이로 통일 시키는데 걸리는 시간 탐색
for height in range(max_h, min_h-1, -1):
    sec = check(height, B)
    if sec < min_sec:
        min_sec = sec
        mlv = height

print(min_sec, mlv)







