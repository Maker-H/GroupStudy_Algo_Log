L = list(input())

stack = []
cnt = 0

for i in range(len(L)):
    if L[i] == '(':
        stack.append(L[i])
        # cnt += 1
    else:
        if L[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)