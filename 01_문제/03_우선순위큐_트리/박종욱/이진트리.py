
def solve(arr,N,T):
    while True:
        if N // 2 == 0:                                 # N // 2 == 0 이되면 끝
            return

        else:
            a_1 = arr[0:(N//2)]                         # 부모노드를 제외한 앞뒤로 나눔
            a_2 = arr[(N//2)+1:N]

            if a_1[(N // 2)//2] == a_1[-((N // 2) // 2) - 1] or a_2[(N // 2)//2] == a_2[-((N // 2) // 2) - 1]:   # a_1과 a_2에 원소가 하나일시
                arr_2[T].append(a_1[(N // 2) // 2])                                                              # 깊이에 맞는 리스트에 앞과 뒤의 원소추가 
                arr_2[T].append(a_2[(N // 2) // 2])
            else:
                arr_2[T].append(a_1[(N // 2)//2])                                                                # a_1과 a_2에 원소가 두개이상일시
                arr_2[T].append(a_1[-((N // 2) // 2) - 1])                      
                arr_2[T].append(a_2[(N // 2) // 2])
                arr_2[T].append(a_2[-((N // 2) // 2) - 1])


            N = N // 2
            T += 1
            solve(a_1,N,T)          # 계속 반복
            solve(a_2,N,T)

        return


import sys
T = int(sys.stdin.readline())                           # 깊이
arr = list(map(int,sys.stdin.readline().split()))
arr_2 = [[] for _ in range(T)]                          # 깊이 순서대로 넣을 리스트 생성            
N = len(arr)                                            # 루트노드 뽑을 인덱스                
arr_2[0].append(arr[N//2])                              # 루트노드 추가

solve(arr,N,1)

for i in range(T):
    print(*arr_2[i])






