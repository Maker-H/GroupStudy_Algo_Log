import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
stack = list()
for _ in range(n) :
    com, *num = input().split()
    if com =="push" :
        stack.append(int(num[0]))
    elif com == "pop" :
        print(stack.pop() if len(stack)>0 else -1)
    elif com == "size" :
        print(len(stack))
    elif com == "empty" :
        print(1 if len(stack) ==0 else 0)
    elif com == "top" :
        print(stack[-1] if len(stack)>0 else -1)