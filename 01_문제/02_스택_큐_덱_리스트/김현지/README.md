#### [1935] 후위 표기식2 / 스택 / 실버3

```python
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
```

🧑‍💻리뷰(jongwook123)

`기호만 존재하는 리스트를 따로만들어 p가 기호내에 존재할 시 first second 를 우선 팝하여 이후에 if 문을 사용하여 기호에따라 연산을 진행하면 코드내의 같은 부분의 반복을 줄일 수 있을 것 같습니다.`

```python
N = int(input())
postfix = list(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))

for i in range(len(postfix)):
    if postfix[i].isalpha():
        postfix[i] = num_list[ord(postfix[i]) - 65]

op = ['+', '-', '*', '/']
stack = []
for p in postfix:
    if p in op:
        first = stack.pop()
        second = stack.pop()
        if p == '+':
            stack.append(second + first)
        elif p == '-':
            stack.append(second - first)
        elif p == '*':
            stack.append(second * first)
        elif p == '/':
            stack.append(second / first)
    else:
        stack.append(p)

print(f'{stack[0]:.2f}')
```

위 리뷰를 통해 코드 내의 불필요한 반복을 줄였습니다.
