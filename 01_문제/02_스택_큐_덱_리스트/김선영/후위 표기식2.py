import sys
input = sys.stdin.readline

n = int(input())                    # 피연산자의 개수
_input = list(map(str, input().rstrip()))
_alpha = []                         # 
for _ in range(n):
    _alpha.append(int(input()))
for idx in range(len(_input)):
    if _input[idx].isalpha():
        _input[idx] = _alpha[ord(_input[idx])-65]

stack = []
for token in _input:
    if str(token) in '+-*/':    # 연산자일 때
        a = stack.pop()         # 피연산자 두 개 pop
        b = stack.pop()

        if token == '-':
            result = b - a
        elif token == '*':
            result = b * a
        elif token == '+':
            result = b + a
        elif token == '/':
            result = b / a

        stack.append(result)
    else:
        stack.append(token)     # 피연산자는 push

print("{:.2f}".format(stack.pop()))
