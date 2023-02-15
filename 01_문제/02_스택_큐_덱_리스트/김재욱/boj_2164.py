from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1): #큐가 없을때까지 반복
    deque.popleft() # 가장 위에 있는 카드 버리기
    move_num = deque.popleft()
    deque.append(move_num) # 위쪽의 카드를 아래로 옮기기
    
print(deque[0])