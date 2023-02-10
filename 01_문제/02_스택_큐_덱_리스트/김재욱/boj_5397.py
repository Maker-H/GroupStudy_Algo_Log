test_cases = int(input())

for _ in range(test_cases):
    left = []
    right = []
    pwd = input()

    for x in pwd:
        if x == ">": # >이면 오른쪽에 있는 것을 왼쪽으로 옮김
            if right:
                left.append(right.pop())
        elif x=="<": # <이면 왼쪽에 있는 것을 오른쪽으로 옮김
            if left:
                right.append(left.pop())
        elif x=="-": # -이면 왼쪽에 있는 것을 pop
            if left:
                left.pop()
        else: # 문자가나오면 왼쪽에 append
            left.append(x)

    print("".join(left)+"".join(reversed(right))) # 스택에 쌓기 때문에 오른쪽은 revers해서 출력