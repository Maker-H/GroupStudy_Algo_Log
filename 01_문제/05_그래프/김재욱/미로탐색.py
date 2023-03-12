import queue


n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
chk = [[0]* m for _ in range(n)]


q = queue.Queue()
q.put([0,0])
chk[0][0] = 1
while not q.empty():
    x, y = q.get()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 만족하는지 확인
        if nx < 0 or nx >= n: continue
        if ny < 0 or ny >= m: continue 
        # 이동할 수 있는 곳인지 방문한 곳인지 확인
        if a[nx][ny] == 0: continue  
        if chk[nx][ny] != 0: continue

        chk[nx][ny] = chk[x][y] + 1
        q.put([nx, ny])

print(chk[n-1][m-1])