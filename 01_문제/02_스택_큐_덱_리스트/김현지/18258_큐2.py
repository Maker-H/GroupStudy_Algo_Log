import sys
from collections import deque

dq = deque()
N = int(input())
for n in range(N):
    com, *num = sys.stdin.readline().split()
    if com == 'push':
        dq.append(*num)
    elif com == 'pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif com == 'size':
        print(len(dq))
    elif com == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif com == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif com == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)