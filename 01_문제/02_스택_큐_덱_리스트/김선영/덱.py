from collections import deque
import sys
input = sys.stdin.readline

d = deque()
n = int(input())
for _ in range(n):
    _input = list(map(str, input().split()))
    if _input[0] == 'push_front':
        d.appendleft(_input[1])
    elif _input[0] == 'push_back':
        d.append(_input[1])
    elif _input[0] == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif _input[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif _input[0] == 'size':
        print(len(d))
    elif _input[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif _input[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)
