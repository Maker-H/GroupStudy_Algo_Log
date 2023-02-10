N = int(input())
postfix = list(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))

for i in range(len(postfix)):
    if postfix[i].isalpha():
        postfix[i] = num_list[ord(postfix[i]) - 65]

stack = []
for p in postfix:
    if p == '+':
        first = stack.pop()
        second = stack.pop()
        stack.append(second+first)
    elif p == '-':
        first = stack.pop()
        second = stack.pop()
        stack.append(second-first)
    elif p == '*':
        first = stack.pop()
        second = stack.pop()
        stack.append(second*first)
    elif p == '/':
        first = stack.pop()
        second = stack.pop()
        stack.append(second/first)
    else:
        stack.append(p)

print(f'{stack[0]:.2f}')
