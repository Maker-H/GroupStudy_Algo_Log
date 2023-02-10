T = int(input())
count = 0
for _ in range(T):
    _input = input()
    stack = []

    for i in _input:
        if not stack:
            stack.append(i)
        else:
            if i =='A':
                if stack[-1] != 'A':
                    stack.append(i)
                else:
                    stack.pop()
            else:
                if stack[-1] != 'B':
                    stack.append(i)
                else:
                    stack.pop()

    else:
        if not stack:
            count +=1
print(count)