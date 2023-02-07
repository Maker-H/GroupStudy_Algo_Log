import sys

T = int(sys.stdin.readline())

a = []                                          # 숫자를 넣을 리스트 생성
for tc in range(T):
    A,*B = sys.stdin.readline().split()         # input 되는 값 두개중 하나를 팩으로 받아서 값이 없어도 에러가 나지않게함

    if A == 'push_back':                        # push_back에서는 append로 가장 뒤에 넣음
        a.append(B)

    if A == 'push_front':                       # push_front에서는 insert로 가장 앞에 넣음
        a.insert(0,B)

    if A == 'pop_front':                        #pop_front에서는 b에 값을 할당해주고 삭제후 b를 출력함
        if len(a) == 0:
            print(-1)
        else:
            b = a[0]
            a.remove(a[0])
            print(*b)

    if A == 'pop_back':                         #pop_back에서는 c에 팝해준값을 할당 c를 출력
        if len(a) == 0
            print(-1)
        else:
            c = a.pop()
            print(*c)


    if A== 'size':                              # 크기
        print(len(a))

    if A == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)

    if A == 'front':                            # 인덱스로 가장앞의 값 출력
        if len(a) == 0:
            print(-1)
        else:
            print(*a[0])

    if A == 'back':
        if len(a) == 0:
            print(-1)
        else:
            print(*a[-1])


