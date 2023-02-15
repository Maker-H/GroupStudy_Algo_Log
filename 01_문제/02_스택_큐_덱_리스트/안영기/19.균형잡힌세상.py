import sys
sys.stdin = open('균형잡힌세상_input.txt', 'r')

while True:
    s = input()
    if s == '.':
        break
    stack = []
    ans = 1
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack or stack[-1] == '[':
                ans = 0
                break
            elif stack[-1] == '(':
                stack.pop()
        elif s[i] == ']':
            if not stack or stack[-1] == '(':
                ans = 0
                break
            elif stack[-1] == '[':
                stack.pop()
    if ans == 1 and not stack:
        print('yes')
    else:
        print('no')




