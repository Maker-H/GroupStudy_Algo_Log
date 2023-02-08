

T = int(input())
for tc in range(T):
    Stack = []
    A = list(input())
    for a in A:
        if a == '(':
            Stack.append(a)
        else:
            if len(Stack) == 0:
                print('NO')
                break
            else:
                Stack.pop()
    else:
        if len(Stack) == 0:
            print('YES')
        else:
            print('NO')