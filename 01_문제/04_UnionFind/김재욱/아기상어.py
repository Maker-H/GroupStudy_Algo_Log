import sys
from collections import deque


input = lambda : sys.stdin.readline().rstrip()

n = int(input())

map = [list(map(int,input().split()))for _ in range(n)]

now_size = 2
now_eat = 0
time =0

dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(n):
        if map[i][j] == 9:
            a, b= i,j

def bfs(a,b,now_size):
    distance = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    q= deque()
    q.append((a,b))
    visited[a][b]=1
    temp = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if map[nx][ny]<= now_size:
                    #통과 가능한지 체크
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] +1
                    if map[nx][ny] < now_size and map[nx][ny] != 0:
                        # 먹을 수 있는지 체크
                        temp.append((nx,ny,distance[nx][ny]))

    return sorted(temp, key=lambda x:(-x[2],-x[0],-x[1]))
    #가장 가까운것, 가장 위쪽, 왼쪽 순으로 정렬

while True:
    shark = bfs(a,b,now_size)

    if len(shark) == 0:
        break

    nx,ny,dist = shark.pop()

    time +=dist

    map[a][b],map[nx][ny] = 0,0
    #상어 원래 위치, 먹은 위치 0으로 초기화
    a,b = nx,ny
    #상어 위치
    now_eat +=1

    if now_size==now_eat:
        now_size+=1
        now_eat=0

print(time)