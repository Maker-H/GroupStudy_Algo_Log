import sys
from collections import deque
sys.stdin = open('AC_input.txt', 'r')

T = int(input())
for testcase in range(T):
    command = list(input())
    N = int(input())

    arr = deque(input()[1:-1].split(','))
    if N == 0:
        arr = deque()

    cnt = 0
    for order in command:
        if order == 'R':
            cnt += 1
        elif order == 'D':
            if arr:
                if cnt % 2:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                break
    else:
        if cnt % 2 == 1:
            arr.reverse()

        print('['+ ','.join(arr) + ']')


