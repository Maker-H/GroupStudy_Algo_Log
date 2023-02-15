T = int(input())
N = list(input())                                       # 후위표기식 받아 리스트 만듬
num = []                                                # 숫자 저장할 리스트


for tc in range(T):                                     # T만큼 반복
    num.append(int(input()))                            # num에 숫자들을 저장


Stack = []                                              # 문자들의 값을 넣을Stack 생성
giho = ['*','+','/','-']                                # 기호



 
for i in N:                                             # 후위 표기식 반복
    if i.isalpha():                                     # 만약 문자면
        Stack.append(num[ord(i) - ord('A')])            # ord사용하여 if A면 num[0]의 값을 가져오게 식 생성 Stack에 추가
    elif i in giho:                                     # 문자가 아니라 기호면
        a = Stack.pop()                                 # 숫자 하나뽑고
        b = Stack.pop()                                 # 다시 하나뽑고
        if i == '*':                                    # 기호에 맞는 값들 계산후 Stack에 저장
            Stack.append(b * a)
        elif i == '+':
            Stack.append(b + a)
        elif i == '/':
            Stack.append(b / a)
        elif i == '-':
            Stack.append(b - a)
print(f'{Stack[0]:.2f}')

