from collections import deque
import sys


T = int(sys.stdin.readline())

a = deque()
for _ in range(T):

    K = sys.stdin.readline().split()

    if K[0] == 'push':
        a.append(int(K[1]))

    elif K[0] == 'pop':
        if len(a) >= 1:
            print(a[0])
            a.popleft()
        else:
            print(-1)

    elif K[0] == 'size':
        print(len(a))

    elif K[0] == 'empty':
        if len(a) >= 1:
            print(0)
        else:
            print(1)

    elif K[0] == 'front':
        if len(a) == 0:
            print(-1)
        else:
            print(a[0])

    elif K[0] == 'back':
        if len(a) == 0:
            print(-1)
        else:
            print(a[-1])