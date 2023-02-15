import sys
input = sys.stdin.readline

equations = input()
stack = []
res = ''

for e in equations:
    if e.isalpha():
        res += e

    else:
        if e == '(': # (가 나오면 무조건 append
            stack.append(e)

        elif e == ')': # (가 나올때까지 pop
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()

        elif e == '/' or e == '*': # 우선순위가 같은것 뽑기
            while stack and (stack[-1] == '/' or stack[-1] == '*'): # 조건 주의
                res += stack.pop()
            stack.append(e)

        elif e == '+' or e == '-': # ( 전까지 우선순위가 높거나 같은거 뽑기
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(e)

while stack:
    res+=stack.pop()

print(res)