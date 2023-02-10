import sys

input = sys.stdin.readline

_input = input().rstrip()
stack = []
count = 0
for i in _input:
    if i == '(': #(가 나오면 무조건 추가
        stack.append(i)
        past = i
    else:
        if past == '(': # )가 나올때 앞의 값이 (이면 레이저이기 때문에 stack에 있는 (개수 만큼 더함
            stack.pop()
            count += len(stack)
            past = i

        else: # ))이게되면 판이 끝이 난것이므로 1을 더 해준다.
            stack.pop()
            count += 1
            past = i

print(count)