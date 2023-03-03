import sys


N, M, B = map(int, sys.stdin.readline().split())

land = [[] for _ in range(N)]
highest_land = 0
lowest_land = 257
block_sum = B
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))

    for one_land in tmp:
        if one_land > highest_land:
            highest_land = one_land
        
        if one_land < lowest_land:
            lowest_land = one_land

        block_sum += one_land

    land[i] = tmp


if highest_land > 256:
    highest_land = lowest_land = 256

ground = 0
min_time =  999999999

for goal in range(lowest_land, highest_land + 1):
    total_time = 0    
    # 현재 블록 + B 보다 땅 높이가 높으면 만들 수 없다
    if block_sum < (goal * N * M):
        break

    # 시간 계산
    for first in range(N):
        for second in range(M):
            if land[first][second] > goal:
                total_time += (land[first][second] - goal) * 2 
            
            elif land[first][second] < goal:
                total_time += (goal - land[first][second]) * 1
    

    # 제일 높은 땅이 있고 시간이 같다면 그 땅 출력해준다
    if min_time >= total_time:
        min_time = total_time
        ground = goal

print(min_time, ground)

    


