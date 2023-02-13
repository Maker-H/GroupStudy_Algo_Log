from collections import deque

N = int(input())
dq = deque()

for n in range(1, N + 1):
    dq.append(n)

while True:
    if dq:
        if len(dq) == 1:
            print(dq[0])
            break
        dq.popleft()
        dq.append(dq.popleft())
    else:
        break