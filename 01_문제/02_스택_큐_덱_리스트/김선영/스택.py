import sys
input = sys.stdin.readline

n = int(input())                        # 주어지는 명령의 수
stack = []

for _ in range(n):
    _input = list(map(str, input().split()))    # 명령 입력 리스트
    if _input[0] == 'push':             # 정수 X를 스택에 넣는 연산이다.
        stack.append(_input[1])
    elif _input[0] == 'pop':            # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if stack:                       # 비어있지 않을 때
            a = stack.pop()             # a = 반환할 값
            print(a)
        else:                           # 비어있을 때
            print(-1)
    elif _input[0] == 'size':           # 스택에 들어있는 정수의 개수를 출력한다.
        print(len(stack))
    elif _input[0] == 'empty':          # 스택이 비어있으면 1, 아니면 0을 출력한다.
        if stack:
            print(0)
        else:
            print(1)
    else:                               # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if stack:
            print(stack[-1])
        else:
            print(-1)

