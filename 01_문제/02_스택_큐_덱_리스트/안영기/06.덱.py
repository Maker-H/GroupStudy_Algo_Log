import sys
from collections import deque
sys.stdin = open('덱.txt', 'r')

n = int(input())

lst = deque()
for i in range(n):
    input_order = sys.stdin.readline().split()
    order = input_order[0]
    if order == 'push_front':
        lst.appendleft(input_order[1])
    elif order == 'push_back':
        lst.append(input_order[1])
    elif order == 'pop_front':
        if len(lst) != 0:
            print(lst[0])
            lst.popleft()
        else:
            print(-1)
    elif order == 'pop_back':
        if len(lst) != 0:
            print(lst[-1])
            lst.pop()
        else:
            print(-1)
    elif order == 'size':
        print(len(lst))
    elif order == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    elif order == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])

