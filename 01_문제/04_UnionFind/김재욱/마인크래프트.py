N, M, B = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
ans = 1e9 # 최소값
idx = 0
for k in range(257):
    plus = 0
    minus  = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= k:
                minus += arr[i][j] - k # k 높이보다 높으면 뺀다

            else:
                plus += k - arr[i][j] # k 높이보다 낮으면 더한다.

    if minus + B >= plus: # B + 뺀 값이 더할려는 값보다 커야지 평평하게 만들 수 있음
        if minus*2 + plus <= ans:
            ans = minus*2 + plus
            idx = k

print(ans, idx)