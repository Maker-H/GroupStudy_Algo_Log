n = int(input())

_list = [list(input()) for _ in range(n)]

for l in _list:
    stack = list()
    for i in l:
        if i == '(': # (이면 무조건 append
            stack.append(i)
        else:
            if len(stack)==0: # )일때 스택이 비어있으면 짝이 맞지 않으므로 no출력
                print('NO')
                break
            stack.pop()

    else:
        if len(stack) == 0: # 모든 과정을 끝냈을때 스택이 비어있지않다면 짝이 맞지 않으므로 no출력
            print('YES')
        else:
            print('NO')