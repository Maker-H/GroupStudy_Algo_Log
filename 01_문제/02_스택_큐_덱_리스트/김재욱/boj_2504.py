import sys
input = sys.stdin.readline

_input = input().rstrip()
ans = 0
tmp = 1
stack = []
for i in range(len(_input)):
    if _input[i] == '(':
        stack.append(_input[i])
        tmp *= 2
    elif _input[i] == '[':
        stack.append(_input[i])
        tmp *= 3
    elif _input[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if _input[i-1] == '(':  
            ans += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if  _input[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3
if stack:
    print(0)
else:
    print(ans)