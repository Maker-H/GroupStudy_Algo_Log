from collections import deque
import sys
input = sys.stdin.readline

d = deque()
n = int(input())
for _ in range(n):
    _input = list(map(str, input().split()))
    if _input[0] == 'push_front':       # 정수 X를 덱의 앞에 넣는다.
        d.appendleft(_input[1])
    elif _input[0] == 'push_back':      # 정수 X를 덱의 뒤에 넣는다.
        d.append(_input[1])
    elif _input[0] == 'pop_front':      # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
        if d:
            print(d.popleft())
        else:                           # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            print(-1)
    elif _input[0] == 'pop_back':       # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 
        if d:
            print(d.pop())
        else:                           # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            print(-1)
    elif _input[0] == 'size':           # 덱에 들어있는 정수의 개수를 출력한다.
        print(len(d))
    elif _input[0] == 'empty':
        if d:                           # 덱이 비어있지 않으면 0을 출력
            print(0)
        else:                           # 덱이 비어있으면 1을 출력
            print(1)
    elif _input[0] == 'front':
        if d:                           # 덱의 가장 앞에 있는 정수를 출력
            print(d[0])
        else:                           # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력
            print(-1)
    else:                               # back: 덱의 가장 뒤에 있는 정수를 출력
        if d:
            print(d[-1])
        else:                           # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력
            print(-1)
