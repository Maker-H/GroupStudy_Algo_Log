Stack = []                                          # 숫자를 쌓을 스택 생성
count = 1                                           # 1부터 세어서 차례대로 넣을 변수 생성
T = int(input())
Stackseq = []                                       # 부호 받을 리스트 생성
can = True                                          # 만약 LIFO가 되지않을경우 False로 변환할 변수
for tc in range(T):
    N = int(input())

    while count <= N:                               # 숫자가 N값과 같을때 까지 그 숫자를 Stack에 쌓는다
        Stack.append(count)                         
        Stackseq.append('+')                        # 부호를 받을 리스트에 +를 추가해줌(push)
        count += 1                                  # 숫자를 + 1 더해준다 
        
    if Stack[-1] == N:                              # 만약 스택의 마지막 값이 N이면
        Stack.pop()                                 # 숫자를 빼고
        Stackseq.append('-')                        # 부호에 - 를 추가한다(pop)
    else:
        can = False                                 # 위의 것들이 이뤄지지 않을경우 False변환
    
if can == False:                                    # False일경우 No출력
    print('NO')
else:
    for i in Stackseq:                              # 추가했던 부호들의 리스트를 프린트한다.
        print(i)