T = list(input())                       # 괄호를 리스트로 쪼개어 넣음

Stack = []                              # 괄호를 넣을 스택을 생성
count = 0                               # 막대기(괄호)의 개수를 셀 변수 생성
for s in range(len(T)):                 
    if T[s] == '(':                     # 만약 '(' 면 스택에 넣어라
        Stack.append(T[s])
    else:
        if T[s-1] == '(':               # 만약 ')'일때 바로전의 값이 '('면 스택에서 뽑아내고 스택 전체의 개수를 더해라 
            Stack.pop()
            count += len(Stack)
        else:                           # 그것이 아니라면 그냥 스택에서 뽑고 카운트 +1 해라
            Stack.pop()
            count += 1
print(count)