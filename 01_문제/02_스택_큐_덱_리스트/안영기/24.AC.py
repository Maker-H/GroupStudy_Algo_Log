import sys
from collections import deque
sys.stdin = open('AC_input.txt', 'r')

T = int(input())
for testcase in range(1, T+1):
    command = list(input())
    N = int(input())
    arr = input().strip('[]').split(',')
    # print(arr, type(arr))
    if N == 0:
        arr = []
    cnt = 0
    for order in command:
        if order == 'R':
            cnt += 1
        elif order == 'D':
            if arr:
                if cnt % 2:
                    arr.pop()
                else:
                    arr.pop(0)
            else:
                print('error')
                break
    else:
        if cnt % 2:
            arr.reverse()
        print('[', ','.join(arr), ']', sep='')



