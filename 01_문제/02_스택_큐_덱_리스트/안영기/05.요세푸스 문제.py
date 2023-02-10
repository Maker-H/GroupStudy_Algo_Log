
N, K = map(int, input().split())
arr = list(range(1,N+1))
yose = []
cnt = 0
while len(arr) != 0:
    cnt += K-1
    if cnt >= len(arr):
        while cnt >= len(arr):
            cnt -= len(arr)
    yose.append(str(arr[cnt]))
    arr.pop(cnt)
print('<', ', '.join(yose), '>', sep = '')



