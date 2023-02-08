import sys
input = sys.stdin.readline

par = input().rstrip()
stack = []
count = 0
for idx in range(len(par)):
    if par[idx] == '(':
        stack.append(par[idx])
    else:
        if par[idx-1] =='(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)
