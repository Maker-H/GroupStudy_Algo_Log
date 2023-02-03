import sys

N = int(input())
stack_list = []
for n in range(N):
    com, *num = sys.stdin.readline().split()
    if com == 'push':
        stack_list.append(*num)
    elif com == 'pop':
        if stack_list:
            print(stack_list.pop())
        else:
            print(-1)
    elif com == 'top':
        if stack_list:
            print(stack_list[-1])
        else:
            print(-1)
    elif com == 'size':
        print(len(stack_list))
    elif com == 'empty':
        if stack_list:
            print(0)
        else:
            print(1)

