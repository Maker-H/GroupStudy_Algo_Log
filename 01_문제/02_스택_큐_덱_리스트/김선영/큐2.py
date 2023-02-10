from collections import deque

import sys
input = sys.stdin.readline

queue = deque()
n = int(input())                                   # 주어지는 명령의 수
for _ in range(n):
    _input = list(map(str, input().split()))        # 명령 입력 리스트
    if _input[0] == 'push':                         # 정수 X를 큐에 넣는 연산이다.
        queue.append(int(_input[1]))
    elif _input[0] == 'pop':                        # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:                                   # 비어있지 않을 때
            a = queue.popleft()                     # a = 반환할 값
            print(a)
        else:                                        # 비어있을 때
            print(-1)
    elif _input[0] == 'size':                       # 큐에 들어있는 정수의 개수를 출력한다.
        print(len(queue))
    elif _input[0] == 'empty':                      # 큐가 비어있으면 1, 아니면 0을 출력한다.
        if queue:
            print(0)
        else:
            print(1)
    elif _input[0] == 'front':                      # 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:                                           # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if queue:
            print(queue[-1])
        else: print(-1)
