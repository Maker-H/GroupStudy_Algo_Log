t = int(input())
for _ in range(t):
    stack = []
    _input = input()
    for par in _input:
        if par == '(':
            stack.append(par)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')