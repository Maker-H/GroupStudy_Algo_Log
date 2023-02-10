import sys
from collections import deque

deq = deque()
N = int(input())
for n in range(N):
    com, *num = sys.stdin.readline().split()
    if com == 'push_front':
        deq.insert(0, *num)
    elif com == 'push_back':
        deq.append(*num)
    elif com == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif com == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif com == 'size':
        print(len(deq))
    elif com == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif com == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif com == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)