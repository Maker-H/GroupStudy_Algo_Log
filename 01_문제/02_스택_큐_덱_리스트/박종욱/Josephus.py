from collections import deque                   # deque import

a = deque()
Jose = []                                       # 탈락자들 넣을 리스트

N,K = map(int,input().split())                  # N : 사람수 K : 탈락자 번호
new = K                                         # new = K 후에 초기화 시켜주기위해 
for i in range(1,N+1):                          # N으로 받은거 a에 저장
    a.append(i)

while len(a) != 0:                              # a의 갯수가 0이 되기전까지
    if new > 1:                                 # 탈락자 번호가 1보다 크면
        a.append(a.popleft())                   # 왼쪽의 원소를 뽑아 다시 a에 넣음
        new -= 1                                # 탈락자 번호 1 감소
    else:                                       # 탈락자 번호가 1이면
        Jose.append(a.popleft())                # 탈락자 뽑아 Jose리스트에 저장
        new = K                                 # 탈락자 번호 리셋
        


print('<',end='')
print(*Jose,sep=', ',end='')
print('>')


