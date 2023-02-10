T = int(input())
count = 0
for _ in range(T):
    _input = input()
    stack = []

    for i in _input:
        if not stack: # 스택이 비어있으면 무조건 추가
            stack.append(i)
        else:
            if i =='A': 
                if stack[-1] != 'A': # BA이면 짝이 맞지 않으므로 A추가
                    stack.append(i)
                else: # AA이므로 pop
                    stack.pop()
            else:
                if stack[-1] != 'B': # AB이면 짝이 맞지 않으므로 A추가
                    stack.append(i)
                else: # BB이므로 pop
                    stack.pop()

    else:
        if not stack: # 스택이 비어있다면 모두 짝이 맞기 때문에 count +1
            count +=1
print(count)