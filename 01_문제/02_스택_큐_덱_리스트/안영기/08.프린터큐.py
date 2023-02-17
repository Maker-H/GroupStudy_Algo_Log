from collections import deque

T = int(input())
for testcase in range(T):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    zero = deque([0] * N)
    zero[M] = 1

    cnt = 0
    while True:
        if arr[0] == max(arr):
            cnt += 1
            if zero[0] == 1:
                print(cnt)
                break
            else:
                arr.popleft()
                zero.popleft()
        else:
            arr.rotate(-1)
            zero.rotate(-1)