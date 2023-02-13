import sys
sys.stdin = open('스택.txt', 'r')

n = int(input())
stack = []
for i in range(n):
    input_order = sys.stdin.readline().split()
    order = input_order[0]
    if order == 'push':
        stack.append(input_order[1])
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])



