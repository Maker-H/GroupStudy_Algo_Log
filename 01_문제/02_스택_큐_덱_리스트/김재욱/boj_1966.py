from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    _list = list(map(int,input().split()))

    Q = deque(_list)
    _list.sort() # 우선순위를 비교하기 위해 정렬
    count = 0
    while Q: # 큐가 비어있기 전까지 반복
        if Q[0] == _list[-1]: # 우선순위가 우선인 숫자가 큐가장 앞에 있는 경우 Pop
            Q.popleft()
            _list.pop()
            count += 1
            if M == 0: # 만약 뽑은 숫자가 뽑을려는 문서일 때
                print(count)
                break
            else:
                M -= 1 # 아니면 뽑으려는 문서의 현재 위치를 나타내기 위해 -1
        else:
            Q.append(Q.popleft()) # 가장 앞의 문서가 우선순위가 아니면 뒤로 보내기
            if M == 0: # 가장 앞의 문서가 뽑으려는 문서이면 가장 뒤로 보내지기 때문에 현재 위치를 가장 뒤로 표시
                M = len(Q)-1 
            else:
                M -= 1 # 뽑으려는 문서의 가장 최근위치 갱신