import sys
input = sys.stdin.readline

par = input().rstrip()
stack = []
count = 0
for idx in range(len(par)):
    if par[idx] == '(':         # '('이 나오면 stack에 push
        stack.append(par[idx])
    else:                       # ')'이 나오면
        if par[idx-1] =='(':    # 바로 앞이 '('이면 레이저이므로
            stack.pop()         # stack에서 레이저를 구성하는 '('를 하나 지우고
            count += len(stack) # stack에 들어있던 '('의 수를 count에 누적
        else:                   # 레이저가 아니면 쇠막대기이므로
            stack.pop()         # stack에서 쇠막대기를 구성하는 '('를 하나 지우고
            count += 1          # 그 막대기의 끝부분의 조각을 하나 count
print(count)
